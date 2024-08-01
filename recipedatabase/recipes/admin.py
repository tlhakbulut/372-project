from django.contrib import admin
from .models import Recipe, FavoriteRecipe

admin.site.register(Recipe)
admin.site.register(FavoriteRecipe)
