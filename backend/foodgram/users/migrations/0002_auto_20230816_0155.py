# Generated by Django 3.2 on 2023-08-15 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={"ordering": ("-pk",)},
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
