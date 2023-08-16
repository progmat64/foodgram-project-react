from rest_framework.routers import DefaultRouter

from django.urls import include, path

from .views import (IngredientViewSet, RecipeViewSet, SubscriptionViewSet,
                    TagViewSet)

router = DefaultRouter()


router.register("tags", TagViewSet, basename="tags")
router.register("recipes", RecipeViewSet, basename="recipes")
router.register("ingredients", IngredientViewSet, basename="ingredients")
router.register("users", SubscriptionViewSet, basename="subscription")


urlpatterns = [path("", include(router.urls))]
