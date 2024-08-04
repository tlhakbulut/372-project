from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('login/', auth_views.LoginView.as_view(template_name='recipes/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', views.user_profile, name='user_profile'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('edit_recipe/<int:recipe_id>/', views.edit_recipe, name='edit_recipe'),
    path('delete_recipe/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
    path('add_favorite/<int:recipe_id>/', views.add_favorite, name='add_favorite'),
    path('rate_recipe/<int:recipe_id>/', views.rate_recipe, name='rate_recipe'),
]
