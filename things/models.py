from django.db import models
from django.db.models import Model
from django.core.validators import MaxValueValidator, MinValueValidator

class Thing(Model):
    name = models.TextField(
        max_length=30,
        blank=False,
        unique=True
    )
    description = models.TextField(
        max_length=120,
        blank=True,
        unique=False
    )
    quantity = models.IntegerField(
        unique=False,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )
