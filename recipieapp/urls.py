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
    path('viewrecipe', views.viewrecipe, name="viewrecipe"),
    path('recipedetails/<int:id>', views.recipedetails, name="recipedetails"),
    path('deleteincredient/<int:id>/<int:pk>', views.deleteincredient, name="deleteincredient"),
    path('userprofile', views.userprofile, name="userprofile"),
    path('sendto/<int:id>', views.sendto, name="sendto"),
]