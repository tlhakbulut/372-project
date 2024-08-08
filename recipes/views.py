from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, RecipeFilterForm
from .models import Recipe, FavoriteRecipe

@login_required
def recipe_list(request):
    query = request.GET.get('q')
    if query:
        recipes = Recipe.objects.filter(name__icontains=query)
    else:
        recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

@login_required
def user_profile(request):
    user_recipes = Recipe.objects.filter(user=request.user)
    favorite_recipes = FavoriteRecipe.objects.filter(user=request.user)
    return render(request, 'recipes/user_profile.html', {
        'user_recipes': user_recipes,
        'favorite_recipes': [fav.recipe for fav in favorite_recipes],
    })

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            messages.success(request, 'Tarif başarıyla eklendi!')
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = RecipeForm()
    return render(request, 'recipes/add_recipe.html', {'form': form})

@login_required
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            updated_recipe = form.save(commit=False)
            if not form.cleaned_data.get('url'):
                updated_recipe.url = recipe.url
            updated_recipe.save()
            messages.success(request, 'Tarif başarıyla güncellendi!')
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/edit_recipe.html', {'form': form, 'recipe': recipe})

@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        recipe.delete()
        return redirect('user_profile')
    return render(request, 'recipes/delete_recipe.html', {'recipe': recipe})

@login_required
def add_favorite(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    favorite, created = FavoriteRecipe.objects.get_or_create(user=request.user, recipe=recipe)
    if created:
        messages.success(request, 'Recipe added to your favorites.')
    else:
        messages.info(request, 'Recipe is already in your favorites.')
    return redirect('recipe_detail', recipe_id=recipe_id)

@login_required
def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

@login_required
def rate_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        rating = int(request.POST.get('rating', 0))
        # Puanı güncelleme işlemi
        if rating > 0 and rating <= 5:
            recipe.rating = (recipe.rating + rating) / 2  # Ortalama puanı güncelleme
            recipe.save()
    return redirect('recipe_detail', recipe_id=recipe_id)

def recipe_filter(request):
    recipes = Recipe.objects.all()
    filter_form = RecipeFilterForm(request.GET)
    
    if filter_form.is_valid():
        
        min_prep_time = filter_form.cleaned_data.get('min_prep_time')
        max_prep_time = filter_form.cleaned_data.get('max_prep_time')
        min_total_time = filter_form.cleaned_data.get('min_total_time')
        max_total_time = filter_form.cleaned_data.get('max_total_time')
        ingredients = filter_form.cleaned_data.get('ingredients')
        min_rating = filter_form.cleaned_data.get('min_rating')
        max_rating = filter_form.cleaned_data.get('max_rating')
        
        
        if min_prep_time is not None:
            recipes = recipes.filter(prep_time__gte=min_prep_time)
        if max_prep_time is not None:
            recipes = recipes.filter(prep_time__lte=max_prep_time)
        if min_total_time is not None:
            recipes = recipes.filter(total_time__gte=min_total_time)
        if max_total_time is not None:
            recipes = recipes.filter(total_time__lte=max_total_time)
        if ingredients:
            recipes = recipes.filter(ingredients__icontains=ingredients)
        if min_rating is not None:
            recipes = recipes.filter(rating__gte=min_rating)
        if max_rating is not None:
            recipes = recipes.filter(rating__lte=max_rating)
    
    context = {
        'recipes': recipes,
        'filter_form': filter_form,
    }
    return render(request, 'recipes/recipe_list.html', context)


