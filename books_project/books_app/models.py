from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.db import models


def validate_pages(value):
    if value <= 0:
        raise ValidationError("Pages cannot be less than or equal to zero!")


class Book(models.Model):
    title = models.CharField(
        max_length=20,
    )
    pages = models.IntegerField(
        validators=(
            MinValueValidator(1),
        ),
    )
    description = models.CharField(
        max_length=100,
        default="",
    )
    author = models.CharField(
        max_length=20,
    )

    def __str__(self) -> str:
        return f"{self.title}"
