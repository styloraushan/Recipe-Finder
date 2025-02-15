from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# API Key (Replace with your valid API Key)
API_KEY = "9cfad92bb48d4c398dbf066de10f40f5"

# Function to fetch recipes
def get_recipes(ingredients, diet):
    url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "apiKey": API_KEY,
        "query": ingredients,
        "diet": diet if diet != "None" else "",
        "number": 10,
        "addRecipeInformation": True
    }
    response = requests.get(url, params=params)
    return response.json() if response.status_code == 200 else {"error": "API request failed"}

# Route for Home Page
@app.route('/')
def index():
    return render_template('index.html')

# Route for processing form submission
@app.route('/search', methods=['POST'])
def search():
    ingredients = request.form.get("ingredients")
    diet = request.form.get("diet")
    recipes = get_recipes(ingredients, diet)
    
    return render_template('result.html', recipes=recipes)

if __name__ == "__main__":
    app.run(debug=True)
