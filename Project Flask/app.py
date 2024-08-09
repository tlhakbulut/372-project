from flask import Flask, render_template, request, redirect, url_for, flash
from recipe_manager import RecipeManager

app = Flask(__name__)
app.secret_key = 'password'  


recipe_manager = RecipeManager("localhost", "root", "1234", "proje_ara_rapor372")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        recipe_data = {
            "recipe_name": request.form['recipe_name'],
            "servings": int(request.form['servings']),
            "rating": float(request.form['rating']),
            "url": request.form['url'],
            "ingredients": request.form['ingredients'].split('\n'),
            "directions": request.form['directions'].split('\n'),
            "nutrition": {
                "calories": float(request.form['calories']),
                "protein": float(request.form['protein']),
                "fat": float(request.form['fat'])
            },
            "timing": {
                "prep": int(request.form['prep_time']),
                "cook": int(request.form['cook_time'])
            }
        }
        recipe_id = recipe_manager.add_recipe(recipe_data)
        if recipe_id:
            flash('Recipe added successfully!', 'success')
            return redirect(url_for('view_recipe', recipe_id=recipe_id))
        else:
            flash('Failed to add recipe.', 'error')
    return render_template('add_recipe.html')

@app.route('/search')
def search():
    query = request.args.get('query', '')
    recipes = recipe_manager.search_recipes(query)
    return render_template('search_results.html', recipes=recipes, query=query)

@app.route('/search_ingredient')
def search_ingredient():
    query = request.args.get('query', '')
    recipes = recipe_manager.search_ingredient(query)
    return render_template('search_results.html', recipes=recipes, query=query)

@app.route('/recipe/<int:recipe_id>')
def view_recipe(recipe_id):
    recipe = recipe_manager.get_recipe(recipe_id)
    if recipe:
        return render_template('view_recipe.html', recipe=recipe)
    else:
        flash('Recipe not found.', 'error')
        return redirect(url_for('index'))

@app.route('/update_recipe/<int:recipe_id>', methods=['GET', 'POST'])
def update_recipe(recipe_id):
    recipe = recipe_manager.get_recipe(recipe_id)
    if not recipe:
        flash('Recipe not found.', 'error')
        return redirect(url_for('index'))

    if request.method == 'POST':
        recipe_data = {
            "recipe_name": request.form['recipe_name'],
            "servings": int(request.form['servings']),
            "rating": float(request.form['rating']),
            "url": request.form['url'],
        }
        if recipe_manager.update_recipe(recipe_id, recipe_data):
            flash('Recipe updated successfully!', 'success')
            return redirect(url_for('view_recipe', recipe_id=recipe_id))
        else:
            flash('Failed to update recipe.', 'error')
    
    return render_template('update_recipe.html', recipe=recipe)

@app.route('/delete_recipe/<int:recipe_id>', methods=['POST'])
def delete_recipe(recipe_id):
    if recipe_manager.delete_recipe(recipe_id):
        flash('Recipe deleted successfully!', 'success')
    else:
        flash('Failed to delete recipe.', 'error')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
