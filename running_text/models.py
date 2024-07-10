from django.core.validators import MaxLengthValidator, MaxValueValidator, MinValueValidator
from django.db import models


class Runtext(models.Model):
    id = models.BigAutoField("id", primary_key=True)
    text = models.CharField(
        "Текст",
        max_length=100,
        validators=[MaxLengthValidator(100)],
    )
    width = models.IntegerField(
        "Ширина",
        blank=False,
        null=True,
        default=100,
        validators=[
            MinValueValidator(50),
            MaxValueValidator(1000),
        ],
    )
    height = models.IntegerField(
        "Высота",
        blank=False,
        null=True,
        default=100,
        validators=[
            MinValueValidator(50),
            MaxValueValidator(1000),
        ],
    )
    duration = models.IntegerField(
        "Длительность",
        blank=False,
        null=True,
        default=3,
        validators=[
            MinValueValidator(2),
            MaxValueValidator(10),
        ],
    )
    font_size = models.IntegerField(
        "Размер текста",
        blank=False,
        null=True,
        default=40,
        validators=[
            MinValueValidator(10),
            MaxValueValidator(200),
        ],
    )
    models.CharField(max_length=7)
    text_color = models.CharField(
        "Цвет текста",
        max_length=7,
        blank=False,
        null=True,
        default="#ffffff",
    )
    background_color = models.CharField(
        "Цвет фона",
        max_length=7,
        blank=False,
        null=True,
        default="#ff0000",
    )
    created_at = models.DateTimeField(
        "Дата запроса",
        auto_now_add=True,
    )
