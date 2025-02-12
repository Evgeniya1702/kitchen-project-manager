from django.shortcuts import render
from catalog.models import DishType, Dish, Cook


def index(request):
    num_dishes = Dish.objects.count()
    num_dishtypes = DishType.objects.count()
    num_cook = Cook.objects.count()
    context = {
        "num_dishes": num_dishes,
        "num_dishtypes": num_dishtypes,
        "num_cook": num_cook,
    }
    return render(request, template_name='catalog/index.html', context=context,)