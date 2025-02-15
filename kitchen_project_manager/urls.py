"""
URL configuration for kitchen_project_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from catalog.views import DishTypeListView, DishListView, DishDetailView, CookListView, CookDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls', namespace='catalog')),
    path('dish_types/', DishTypeListView.as_view(), name='dishtype_list'),
    path('dishes/', DishListView.as_view(), name='dish_list'),
    path('dishes/<int:pk>/', DishDetailView.as_view(), name='dish_detail'),
    path('cooks/', CookListView.as_view(), name='cook_list'),
    path('cooks/<int:pk>/', CookDetailView.as_view(), name='cook_detail'),
]