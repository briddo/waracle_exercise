
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Cake(models.Model):
    name = models.CharField(max_length=30)
    comment = models.CharField(max_length=200)
    image = models.ImageField()
    yum_factor = models.PositiveSmallIntegerField(
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(1)],
    )

    def __str__(self):
        return self.name
