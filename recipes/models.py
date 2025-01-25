from django.db import models

from accounts.models import CustomUser


class Recipe(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="recipes")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    servings = models.PositiveIntegerField(default=1)
    calories = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    carbs = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")
    name = models.CharField(max_length=255)
    quantity = models.FloatField()
    unit = models.CharField(max_length=50, choices=[
        ('g', 'grams'),
        ('kg', 'kilograms'),
        ('ml', 'milliliters'),
        ('l', 'liters'),
        ('tbsp', 'tablespoons'),
        ('tsp', 'teaspoons'),
        ('cup', 'cups'),
        ('oz', 'ounces'),
        ('lb', 'pounds')
    ])

    def __str__(self):
        return f"{self.quantity} {self.unit} {self.name}"