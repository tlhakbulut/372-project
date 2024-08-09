import mysql.connector
from mysql.connector import Error

class RecipeManager:
    def __init__(self, host, user, password, database):
        self.connection = None
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='1234',
                database='proje_ara_rapor372'
            )
            print("Successfully connected to the database")
        except Error as e:
            print(f"Error connecting to MySQL database: {e}")

    def add_recipe(self, recipe_data):
        if self.connection is None or not self.connection.is_connected():
            print("Database connection is not established.")
            return

        try:
            cursor = self.connection.cursor()

            # Insert into Recipe table
            recipe_query = """INSERT INTO recipe (recipe_name, servings, rating, url)
                              VALUES (%s, %s, %s, %s, %s)"""
            recipe_values = (recipe_data['recipe_name'], recipe_data['servings'], 
                             recipe_data['rating'], recipe_data['url'])
            cursor.execute(recipe_query, recipe_values)
            recipe_id = cursor.lastrowid

            # Insert ingredients
            for ingredient in recipe_data['ingredients']:
                ingredient_query = "INSERT INTO ingredients (ingredient) VALUES (%s)"
                cursor.execute(ingredient_query, (ingredient,))
                ingredient_id = cursor.lastrowid
                
                includes_query = "INSERT INTO includes (ingredient_id, include_recipe_id) VALUES (%s, %s)"
                cursor.execute(includes_query, (ingredient_id, recipe_id))

            # Insert directions
            for direction in recipe_data['directions']:
                direction_query = "INSERT INTO directions (directions_recipe_id, direction) VALUES (%s, %s)"
                cursor.execute(direction_query, (recipe_id, direction))

            # Insert nutrition
            for nutrient, amount in recipe_data['nutrition'].items():
                nutrition_query = """INSERT INTO nutrition (nutrition_recipe_id, nutrient, amount)
                                     VALUES (%s, %s, %s)"""
                cursor.execute(nutrition_query, (recipe_id, nutrient, amount))

            # Insert timing
            for timing_type, time in recipe_data['timing'].items():
                timing_query = """INSERT INTO timing (timing_recipe_id, timing_type, minute)
                                  VALUES (%s, %s, %s)"""
                cursor.execute(timing_query, (recipe_id, timing_type, time))

            self.connection.commit()
            print(f"Recipe added successfully with ID: {recipe_id}")
            return recipe_id

        except Error as e:
            print(f"Error adding recipe: {e}")
            self.connection.rollback()
        finally:
            cursor.close()

    def update_recipe(self, recipe_id, recipe_data):
        if self.connection is None or not self.connection.is_connected():
            print("Database connection is not established.")
            return

        try:
            cursor = self.connection.cursor()

            update_query = """UPDATE recipe 
                              SET recipe_name = %s, servings = %s, rating = %s, url = %s
                              WHERE recipe_id = %s"""
            update_values = (recipe_data['recipe_name'], recipe_data['servings'], 
                             recipe_data['rating'], recipe_data['url'], recipe_id)
            cursor.execute(update_query, update_values)

            self.connection.commit()
            print(f"Recipe with ID {recipe_id} updated successfully")
            return True

        except Error as e:
            print(f"Error updating recipe: {e}")
            self.connection.rollback()
            return False
        finally:
            cursor.close()

    def delete_recipe(self, recipe_id):
        if self.connection is None or not self.connection.is_connected():
            print("Database connection is not established.")
            return

        try:
            cursor = self.connection.cursor()

            delete_query = "DELETE FROM recipe WHERE recipe_id = %s"
            cursor.execute(delete_query, (recipe_id,))

            self.connection.commit()
            print(f"Recipe with ID {recipe_id} deleted successfully")
            return True

        except Error as e:
            print(f"Error deleting recipe: {e}")
            self.connection.rollback()
            return False
        finally:
            cursor.close()

    def search_recipes(self, search_term):
        if self.connection is None or not self.connection.is_connected():
            print("Database connection is not established.")
            return

        try:
            cursor = self.connection.cursor(dictionary=True)

            search_query = "SELECT * FROM recipe WHERE recipe_name LIKE %s"
            cursor.execute(search_query, (f"%{search_term}%",))

            recipes = cursor.fetchall()
            return recipes

        except Error as e:
            print(f"Error searching recipes: {e}")
        finally:
            cursor.close()

    def search_ingredient(self, search_term):
        if self.connection is None or not self.connection.is_connected():
            print("Database connection is not established.")
            return
    
        try:
            cursor = self.connection.cursor(dictionary=True)

            search_query = """SELECT r.recipe_id, r.recipe_name, r.servings, r.rating, r.url
                              FROM recipe r
                              JOIN includes i ON r.recipe_id = i.include_recipe_id
                              JOIN ingredients ing ON i.ingredient_id = ing.ingredient_id
                              WHERE ing.ingredient LIKE %s"""
            cursor.execute(search_query, (f"%{search_term}%",))

            recipes = cursor.fetchall()
            return recipes
        
        except Error as e:
            print(f"Error searching recipes: {e}")
        finally:
            cursor.close()


    def get_recipe(self, recipe_id):
        if self.connection is None or not self.connection.is_connected():
            print("Database connection is not established.")
            return

        try:
            cursor = self.connection.cursor(dictionary=True)

            recipe_query = "SELECT * FROM recipe WHERE recipe_id = %s"
            cursor.execute(recipe_query, (recipe_id,))
            recipe = cursor.fetchone()

            if recipe:
                # Fetch ingredients
                ingredient_query = """SELECT i.ingredient 
                                      FROM ingredients i 
                                      JOIN includes inc ON i.ingredient_id = inc.ingredient_id 
                                      WHERE inc.include_recipe_id = %s"""
                cursor.execute(ingredient_query, (recipe_id,))
                recipe['ingredients'] = [row['ingredient'] for row in cursor.fetchall()]

                # Fetch directions
                direction_query = "SELECT direction FROM directions WHERE directions_recipe_id = %s"
                cursor.execute(direction_query, (recipe_id,))
                recipe['directions'] = [row['direction'] for row in cursor.fetchall()]

                # Fetch nutrition
                nutrition_query = "SELECT nutrient, amount FROM nutrition WHERE nutrition_recipe_id = %s"
                cursor.execute(nutrition_query, (recipe_id,))
                recipe['nutrition'] = {row['nutrient']: row['amount'] for row in cursor.fetchall()}

                # Fetch timing
                timing_query = "SELECT timing_type, minute FROM timing WHERE timing_recipe_id = %s"
                cursor.execute(timing_query, (recipe_id,))
                recipe['timing'] = {row['timing_type']: row['minute'] for row in cursor.fetchall()}

            return recipe

        except Error as e:
            print(f"Error fetching recipe: {e}")
        finally:
            cursor.close()

    def __del__(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Database connection closed.")

