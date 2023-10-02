from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('index', views.index, name="index"),
    path('create_recipes', views.create_recipies, name="create_recipies"),
    path('create_recipe2', views.create_recipe2, name="create_recipe2"),
    path('delete_incredient/<int:id>', views.delete_incredient, name="delete_incredient"),
    
]