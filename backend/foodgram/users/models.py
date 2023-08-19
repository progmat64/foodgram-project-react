from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(
        max_length=254, unique=True, verbose_name="Почта"
    )
    username = models.CharField(
        max_length=150, unique=True, verbose_name="Имя пользователя"
    )
    first_name = models.CharField(max_length=150, verbose_name="Имя")
    last_name = models.CharField(max_length=150, verbose_name="Фамилия")
    password = models.CharField(max_length=150, verbose_name="Пароль")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name", "password"]

    class Meta:
        ordering = ("-pk",)
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
