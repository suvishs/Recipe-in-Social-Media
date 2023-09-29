from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from recipieapp.models import *

# Create your views here.

def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')

        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already Taken")
                return render(request, "register.html")
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Both passwords are not matching")
            return render(request, "register.html")
    return render(request, "register.html")

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request, 'Username or password incorrect')
            return render(request, "login.html")
    return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect('index')

def create_recipies(request):
    if request.method == "POST":
        name = request.POST.get("name")
        note = request.POST.get("note")
        image = request.FILES["image"]
        recipe = Recipe(name=name, note=note, image=image, usr=request.user)
        recipe.save()
        messages.info(request, "Recipe first step successful...")
        return redirect("create_recipe2")
    return render(request, "create_recipes.html")

def create_recipe2(request):
    recipes = Recipe.objects.filter(usr=request.user)
    if request.method == "POST":
        pass
    return render(request, "create_recipe2.html", {"recipes":recipes})