from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    prep_time = models.IntegerField()
    cook_time = models.IntegerField()
    total_time = models.IntegerField()
    servings = models.IntegerField()
    ingredients = models.TextField()
    directions = models.TextField()
    rating = models.FloatField()
    url = models.URLField(blank=True, null=True)
    cuisine_path = models.CharField(max_length=100)
    calories = models.IntegerField(blank=True, null=True)
    protein = models.CharField(max_length=100, blank=True, null=True)
    fat = models.CharField(max_length=100, blank=True, null=True)
    nutrition = models.JSONField(blank=True, null=True)  # Nutrition alanını isteğe bağlı hale getiriyoruz

    def __str__(self):
        return self.name

class FavoriteRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.recipe.name}"
