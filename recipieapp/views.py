from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from recipieapp.models import *

# Create your views here.

def index(request):
    users = User.objects.all()
    return render(request, "index.html", {"users":users})

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
        if LastRecipeName.objects.filter(usr=request.user).exists():
            lastname = LastRecipeName.objects.filter(usr=request.user).first()
            lastname.last_name = name
            lastname.save()
        else:
            lastname = LastRecipeName(last_name=name, usr=request.user)
            lastname.save()
        messages.info(request, "Recipe first step successful...")
        return redirect("create_recipe2")
    return render(request, "create_recipes.html")

def create_recipe2(request):
    if request.method == "POST":
        recipe_name = request.POST.get("recipe_name")
        name = request.POST.get("name")
        rawmaterial_name = request.POST.get("rawmaterial_name")
        quantity = request.POST.get("quantity")
        quantity_type = request.POST.get("quantity_type")
        if recipe_name != "None":
            recipe = Recipe.objects.get(name=recipe_name,usr=request.user)
            recipes = RecipeRawmaterials(name=rawmaterial_name,
                                        quantity=quantity,
                                        quantity_type=quantity_type,
                                        usr=request.user,
                                        recipe=recipe)
            recipes.save()
            if LastRecipeName.objects.filter(usr=request.user).exists():
                lastname = LastRecipeName.objects.filter(usr=request.user).first()
                lastname.last_name = recipe_name
                lastname.save()
            else:
                lastname = LastRecipeName(last_name=recipe_name, usr=request.user)
                lastname.save()
            messages.info(request, "Recipe added successfully...")
            return redirect("create_recipe2")
        else:
            if Recipe.objects.filter(name=name).exists():
                recip = Recipe.objects.filter(name=name).first()
                recipes = RecipeRawmaterials(name=rawmaterial_name,
                                        quantity=quantity,
                                        quantity_type=quantity_type,
                                        usr=request.user,
                                        recipe=recip)
                recipes.save()
                if LastRecipeName.objects.filter(usr=request.user).exists():
                    lastname = LastRecipeName.objects.filter(usr=request.user).first()
                    lastname.last_name = name
                    lastname.save()
                else:
                    lastname = LastRecipeName(last_name=name, usr=request.user)
                    lastname.save()
            else:
                messages.info(request, "Recipe is not found...")
                return redirect("create_recipe2")
    if LastRecipeName.objects.filter(usr=request.user):
        last_name = LastRecipeName.objects.filter(usr=request.user).first()
        last_recipe = Recipe.objects.get(name=last_name.last_name,usr=request.user)
        last_incredients = RecipeRawmaterials.objects.filter(recipe=last_recipe, usr= request.user)
        recipez = Recipe.objects.filter(usr=request.user)
        
        return render(request, "create_recipe2.html", {"recipes":recipez, 
                                                       "last_name":last_name,
                                                    #    "last_recipe":last_recipe,
                                                       "last_incredients":last_incredients})
    else:
        return render(request, "create_recipe2.html", {"recipes":recipes})
    
def delete_incredient(request,id):
    incredient = RecipeRawmaterials.objects.get(id=id)
    incredient.delete()
    messages.info(request, "incredient deleted successfully...")
    return redirect("create_recipe2")

def viewrecipe(request):
    if Recipe.objects.filter(usr=request.user).exists():
        recipes = Recipe.objects.filter(usr=request.user)
        return render(request, "viewrecipe.html",{"recipes":recipes})
    else:
        return render(request, "viewrecipe.html")
    
def recipedetails(request,id):
    recipe = Recipe.objects.get(id=id)
    details = RecipeRawmaterials.objects.filter(recipe=recipe)  
    return render(request, "recipedetails.html",{"recipe":recipe,"details":details})

def deleteincredient(request,id, pk):
    incredient = RecipeRawmaterials.objects.get(id=id)
    incredient.delete()
    return redirect(f"/recipedetails/{int(pk)}")

def userprofile(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phonenumber = request.POST.get("phonenumber")
        profilepicture = request.FILES["profilepicture"]
        user_profile = UserProfile(name=name, phonenumber=phonenumber, profilepicture=profilepicture, usr=request.user)
        user_profile.save()
        messages.info(request, "User profile created successfuly...")
        return redirect("index")
    return render(request, "userprofile.html")

def sendto(request,id):
    return render(request, "message.html")