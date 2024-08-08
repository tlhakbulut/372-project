from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    name = forms.CharField(label='Tarif adı')
    prep_time = forms.IntegerField(label='Hazırlama süresi (dakika)')
    cook_time = forms.IntegerField(label='Pişirme süresi (dakika)')
    total_time = forms.IntegerField(label='Toplam süre (dakika)')
    servings = forms.IntegerField(label='Porsiyon sayısı')
    ingredients = forms.CharField(label='Malzemeler', widget=forms.Textarea)
    directions = forms.CharField(label='Yapım adımları', widget=forms.Textarea)
    rating = forms.FloatField(label='Puan')
    url = forms.URLField(label='URL', required=False)
    cuisine_path = forms.CharField(label='Mutfak türü')
    calories = forms.IntegerField(label='Kalori', required=False)
    protein = forms.CharField(label='Protein', required=False)
    fat = forms.CharField(label='Yağ', required=False)

    class Meta:
        model = Recipe
        fields = ['name', 'prep_time', 'cook_time', 'total_time', 'servings', 'ingredients', 'directions', 'rating', 'url', 'cuisine_path', 'calories', 'protein', 'fat']


class RecipeFilterForm(forms.Form):
    
    min_prep_time = forms.IntegerField(required=False, label='Minimum Hazırlama Süresi (dakika)')
    max_prep_time = forms.IntegerField(required=False, label='Maksimum Hazırlama Süresi (dakika)')
    min_total_time = forms.IntegerField(required=False, label='Minimum Toplam Süresi (dakika)')
    max_total_time = forms.IntegerField(required=False, label='Maksimum Toplam Süresi (dakika)')
    ingredients = forms.CharField(required=False, label='Malzemeler', widget=forms.Textarea)
    min_rating = forms.FloatField(required=False, label='Minimum Puan')
    max_rating = forms.FloatField(required=False, label='Maksimum Puan')
