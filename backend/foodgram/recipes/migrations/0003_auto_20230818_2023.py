# Generated by Django 3.2.16 on 2023-08-18 17:23

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("recipes", "0002_auto_20230817_0053"),
    ]

    operations = [
        migrations.AlterField(
            model_name="favorite",
            name="user",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="favorite",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="cooking_time",
            field=models.PositiveSmallIntegerField(
                validators=[django.core.validators.MinValueValidator(1)]
            ),
        ),
        migrations.AlterField(
            model_name="recipeingredient",
            name="amount",
            field=models.PositiveSmallIntegerField(
                validators=[django.core.validators.MinValueValidator(1)]
            ),
        ),
        migrations.AlterField(
            model_name="recipeingredient",
            name="recipe",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="recipe",
                to="recipes.recipe",
            ),
        ),
        migrations.AlterField(
            model_name="shoppinglist",
            name="user",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="shopping_list",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]