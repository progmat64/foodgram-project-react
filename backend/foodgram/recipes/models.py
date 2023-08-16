from django.core.validators import MinValueValidator
from django.db import models

from users.models import User


class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True)
    color = models.CharField(max_length=7, unique=True)
    slug = models.SlugField(unique=True, max_length=200)


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    measurement_unit = models.CharField(max_length=200)

    class Meta:
        unique_together = ("name", "measurement_unit")

    def __str__(self):
        return self.name


class Recipe(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe"
    )
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="recipes/")
    text = models.TextField()
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name="recipe_ingredients",
        through="recipes.RecipeIngredient",
    )
    tags = models.ManyToManyField(Tag, related_name="tags")
    cooking_time = models.IntegerField(validators=(MinValueValidator(1),))


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, related_name="ingredient"
    )
    amount = models.IntegerField(validators=(MinValueValidator(1),))

    class Meta:
        unique_together = ("recipe", "ingredient")


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="favorite",
        blank=True,
    )

    class Meta:
        unique_together = ("user", "recipe")


class Subscribe(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="subscriber", blank=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="subscribed", blank=True
    )

    class Meta:
        unique_together = ("user", "author")


class ShoppingList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="shopping_list"
    )

    class Meta:
        unique_together = ("user", "recipe")
