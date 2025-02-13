from django.db.models import Prefetch
from django.shortcuts import render
from django.views import generic

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


class DishListView(generic.ListView):
    model = Dish
    queryset = Dish.objects.all().order_by('name')
    paginate_by = 10

class DishDetailView(generic.DetailView):
    model = Dish
    queryset = Dish.objects.select_related('dish_type').all().order_by('name')

class DishTypeListView(generic.ListView):
    model = DishType
    queryset = DishType.objects.all().order_by('name')
    paginate_by = 10

class CookListView(generic.ListView):
    model = Cook
    queryset = Cook.objects.all().order_by('username')
    paginate_by = 10

class CookDetailView(generic.DetailView):
    model = Cook
    queryset = Cook.objects.prefetch_related('dishes__dish_type')