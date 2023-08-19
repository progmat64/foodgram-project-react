from django.contrib import admin

from .models import (Favorite, Ingredient, Recipe, RecipeIngredient,
                     ShoppingList, Subscribe, Tag)


class IngredientInline(admin.TabularInline):
    model = RecipeIngredient


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "color", "slug")


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name", "measurement_unit")
    search_fields = ("name",)


@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ("recipe", "ingredient", "amount")

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related("recipe", "ingredient")
        return queryset


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "author",
        "name",
        "image",
        "text",
        "cooking_time",
        "view_favorite",
    )
    search_fields = ("name",)
    list_filter = ("tags", "author")
    inlines = (IngredientInline,)

    def view_favorite(self, obj):
        return Favorite.objects.filter(recipe=obj).count()

    view_favorite.short_description = "favorites"

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related("author").prefetch_related(
            "ingredients", "tags"
        )
        return queryset


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ("user", "recipe")


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ("user", "author")

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related("user", "author")
        return queryset


@admin.register(ShoppingList)
class ShoppingListAdmin(admin.ModelAdmin):
    list_display = ("user", "recipe")

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related("user", "recipe")
        return queryset
