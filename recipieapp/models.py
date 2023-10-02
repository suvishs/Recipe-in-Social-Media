from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class LastRecipeName(models.Model):
    last_name = models.CharField(max_length=50, null=True)
    usr = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)

class Recipe(models.Model):
    name = models.CharField(max_length=50, null=True)
    note = models.CharField(max_length=250, null=True)
    image = models.ImageField(upload_to="recipe_image",null=True)
    calories = models.CharField(max_length=50, null=True)
    neutrions = models.CharField(max_length=50, null=True)
    usr = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
class RecipeRawmaterials(models.Model):
    name = models.CharField(max_length=50,null=True)
    quantity = models.IntegerField(null=True)
    quantity_type = models.CharField(max_length=50, null=True)
    usr = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,null=True,blank=True)

