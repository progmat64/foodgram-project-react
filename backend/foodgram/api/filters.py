from django_filters.rest_framework import FilterSet, filters
from rest_framework.filters import SearchFilter

from recipes.models import Recipe
from users.models import User


class RecipeFilter(FilterSet):
    tags = filters.AllValuesMultipleFilter(field_name="tags__slug")
    author = filters.ModelChoiceFilter(queryset=User.objects.all())
    are_favorited = filters.BooleanFilter(method="filter_are_favorited")
    are_in_shopping_cart = filters.BooleanFilter(
        method="filter_are_in_shopping_cart"
    )

    class Meta:
        model = Recipe
        fields = ("author", "tags")

    def filter_are_favorited(self, queryset, name, value):
        if value and not self.request.user.is_anonymous:
            return queryset.filter(favorite__user=self.request.user)
        return queryset

    def filter_are_in_shopping_cart(self, queryset, name, value):
        if value and not self.request.user.is_anonymous:
            return queryset.filter(shopping_cart__user=self.request.user)
        return queryset


class NameSearchFilter(SearchFilter):
    search_param = "name"
