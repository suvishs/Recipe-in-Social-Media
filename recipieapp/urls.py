from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('index', views.index, name="index"),
    path('create_recipies', views.create_recipies, name="create_recipies"),
    path('create_recipe2', views.create_recipe2, name="create_recipe2"),
    
]