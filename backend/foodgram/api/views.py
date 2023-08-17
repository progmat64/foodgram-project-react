import io

from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import (GenericViewSet, ModelViewSet,
                                     ReadOnlyModelViewSet)

from django.db.models import Count, Exists, OuterRef
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from recipes.models import (Favorite, Ingredient, Recipe, ShoppingList,
                            Subscribe, Tag)
from users.models import User

from .filters import NameSearchFilter, RecipeFilter
from .pagination import CustomPagination
from .permissions import IsAuthorOrReadOnlyPermission
from .serializers import (IngredientSerializer, RecipeSerializer,
                          ShortRecipeSerializer, SubscribeSerializer,
                          TagSerializer)


class TagViewSet(ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None


class RecipeViewSet(ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnlyPermission,
    )
    filter_class = RecipeFilter

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            queryset = self.queryset
        else:
            queryset = self.queryset.annotate(
                is_favorited=Exists(
                    Favorite.objects.filter(
                        recipe__pk=OuterRef("pk"), user=user
                    )
                ),
                is_in_shopping_cart=Exists(
                    ShoppingList.objects.filter(
                        recipe__pk=OuterRef("pk"), user=user
                    )
                ),
            )
        return queryset

    @action(detail=True, methods=["post", "delete"])
    def favorite(self, request, pk):
        if request.method == "POST":
            return self.add_or_delete_object(Favorite, request, pk)
        return self.add_or_delete_object(Favorite, request, pk, delete=True)

    @action(detail=True, methods=["post", "delete"])
    def shopping_cart(self, request, pk):
        if request.method == "POST":
            return self.add_or_delete_object(ShoppingList, request, pk)
        return self.add_or_delete_object(
            ShoppingList, request, pk, delete=True
        )

    @action(detail=False)
    def download_shopping_cart(self, request):
        user = request.user

        if user.is_anonymous:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        buffer = io.StringIO()
        buffer.write("Список покупок:\n")
        ingredients = {}
        shopping = ShoppingList.objects.filter(user=user)

        for shopping_recipe in shopping:
            for (
                ingredient
            ) in shopping_recipe.recipe.recipeingredient_set.all():
                ing_obj = ingredient.ingredient
                amount = ingredient.amount
                ingredients[ing_obj] = ingredients.get(ing_obj, 0) + (
                    amount or 0
                )

        for ingredient, amount in ingredients.items():
            line = f"{ingredient} — {amount} {ingredient.measurement_unit}"
            buffer.write(line + "\n")

        response = HttpResponse(buffer.getvalue(), content_type="text/plain")
        response[
            "Content-Disposition"
        ] = 'attachment; filename="shopping_list.txt"'
        return response

    def add_or_delete_object(self, model, request, pk, delete=False):
        if delete:
            obj = model.objects.filter(user=request.user, recipe=pk)
            if obj.exists():
                obj.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(status=status.HTTP_400_BAD_REQUEST)

        else:
            if not model.objects.filter(user=request.user, recipe=pk).exists():
                obj = model.objects.create(
                    user=request.user, recipe=get_object_or_404(Recipe, id=pk)
                )
                serializer = ShortRecipeSerializer(obj.recipe)
                return Response(
                    serializer.data, status=status.HTTP_201_CREATED
                )
            return Response(status=status.HTTP_400_BAD_REQUEST)


class IngredientViewSet(ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    pagination_class = None
    filter_backends = (NameSearchFilter,)
    search_fields = ("name",)


class SubscriptionViewSet(GenericViewSet):
    serializer_class = SubscribeSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return (
            Subscribe.objects.filter(user=user)
            .annotate(recipes_count=Count("author__recipe"))
            .annotate(
                is_subscribed=Exists(
                    Subscribe.objects.filter(
                        user=user, author=OuterRef("author")
                    )
                )
            )
        )

    @action(detail=True, methods=("post", "delete"))
    def subscribe(self, request, pk=None):
        user = request.user
        author = get_object_or_404(User, id=pk)
        subscriptions = Subscribe.objects.filter(user=user, author=author)

        if request.method == "POST":
            if user == author or subscriptions.exists():
                return Response(status=status.HTTP_400_BAD_REQUEST)
            subscribe = Subscribe.objects.create(user=user, author=author)
            serializer = SubscribeSerializer(
                subscribe,
                context={
                    "request": request,
                    "is_subscribed": True,
                    "recipes_count": Recipe.objects.filter(
                        author=author
                    ).count(),
                },
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        subscriptions.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False)
    def subscriptions(self, request):
        subscriptions = self.get_queryset()
        paginator = CustomPagination()
        paginated_subscriptions = paginator.paginate_queryset(
            subscriptions, request
        )
        serializer = SubscribeSerializer(
            paginated_subscriptions, context={"request": request}, many=True
        )
        return paginator.get_paginated_response(serializer.data)
