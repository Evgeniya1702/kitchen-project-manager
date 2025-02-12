from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from catalog import models
from catalog.models import Dish, DishType, Cook


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    search_fields = ("name",)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "dish_type",)
    lister_filter = ("dish_type",)
    search_fields = ("name", "description",)


@admin.register(Cook)
class CookAdmin(UserAdmin):
    model = Cook
    fieldsets = list(UserAdmin.fieldsets) + [
        (("Additional Information"), {"fields": ("year_of_experience",)})
    ]
    add_fieldsets = list(UserAdmin.fieldsets) + [
        (("Additional Information"), {"fields": ("year_of_experience",)})
    ]
    list_display = ("id", "username", "email", "year_of_experience")
    search_fields = ("username", "email",)

