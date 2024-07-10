from django.core.validators import MaxLengthValidator
from django.db import models


class Runtext(models.Model):
    id = models.BigAutoField("id", primary_key=True)
    text = models.CharField(
        "Текст", max_length=100, validators=[MaxLengthValidator(100)]
    )
    created_at = models.DateTimeField(
        "Дата запроса",
        auto_now_add=True,
    )
