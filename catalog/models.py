from django.contrib.auth.models import AbstractUser
from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    year_of_experience = models.IntegerField()
    groups = models.ManyToManyField("auth.Group",
                                    related_name="cooks",
                                    blank=True,)
    user_permissions = models.ManyToManyField("auth.Permission",
                                              related_name="cook_user_permissions",
                                              blank=True,)

    def __str__(self):
        return f"{self.username} ({self.year_of_experience} years exp)"


class Dish(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE, related_name="dishes")
    cooks = models.ManyToManyField(Cook, related_name="dishes")

    def __str__(self):
        return self.name
