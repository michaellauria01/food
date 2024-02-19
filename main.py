import json
import os
import requests
from bs4 import BeautifulSoup

def main():
    recipe_to_ingredients = getHTM()

    # Write the dictionary to a JSON file
    with open('recipes.json', 'w', encoding='utf-8') as json_file:
        json.dump(recipe_to_ingredients, json_file, ensure_ascii=False, indent=4)

    print("Recipes have been saved to recipes.json")
    for i in master_list:
        print(i)

def getHTM():
    directory_path =  os.getcwd()+'/htm'

    # Iterate over each file in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith(".html") or filename.endswith(".htm"):
            file_path = os.path.join(directory_path, filename)


            # Open and read the HTML file
            with open(file_path, 'r', encoding='utf-8') as file:
                amt_to_ingredient = dict()

                content = file.read()

                # Parse the HTML content with BeautifulSoup
                soup = BeautifulSoup(content, 'html.parser')

                recipe = soup.select_one('.ba-recipe-title__main').get_text().strip()

                # Extract ingredient list
                # Modify the selector based on the HTML structure of your files
                ingredients = soup.select('.ba-info-list__item')
                ingredient_list = [ingredient.get_text().strip() for ingredient in ingredients]

                for ingredient in ingredient_list:
                    ingredient_split = ingredient.split("\n\n")
                    amt_to_ingredient[ingredient_split[1].strip()] = ingredient_split[0].replace("\n", " ")
                    master_list.add(ingredient_split[1].strip())

                recipe_to_ingredients[recipe] = amt_to_ingredient
                recipe_to_ingredients.update(recipe_to_ingredients)
    return recipe_to_ingredients

def getURL():
    file_path = 'recipe_url.json'

    with open(file_path, 'r') as file:
        recipe_url = json.load(file)

    # Extract the URLs
    recipes = recipe_url['recipes']

    return [recipe.get('url') for recipe in recipes]

if __name__ == '__main__':
    recipe_to_ingredients = dict()
    master_list = set()
    main()
