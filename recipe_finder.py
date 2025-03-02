import requests

def find_recipe(ingredients, api_key):
    """
    Search Spoonacular for recipes that match the given ingredients.
    Returns the first recipe found.
    """
    url = "https://api.spoonacular.com/recipes/findByIngredients"
    params = {
        "ingredients": ingredients,
        "number": 1,           # Limit to one recipe
        "ranking": 1,
        "ignorePantry": True,  # Skip common pantry items
        "apiKey": api_key
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("Error: Could not retrieve recipes (Status code:", response.status_code, ")")
        return None
    data = response.json()
    if not data:
        print("No recipes found for the provided ingredients.")
        return None
    return data[0]

def get_recipe_information(recipe_id, api_key):
    """
    Retrieve detailed information (including instructions and ingredients)
    about a recipe using its recipe ID.
    """
    url = f"https://api.spoonacular.com/recipes/{recipe_id}/information"
    params = {"apiKey": api_key}
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("Error: Could not retrieve recipe details (Status code:", response.status_code, ")")
        return None
    return response.json()

def main():
    print("Welcome to the AI Recipe Finder!")
    # Ask the user for ingredients (comma-separated)
    ingredients = input("Enter your ingredients (separated by commas): ").strip()
    # Ask the user for their Spoonacular API key
    api_key = input("Enter your Spoonacular API Key: ").strip()
    
    # Search for a recipe using the ingredients
    recipe = find_recipe(ingredients, api_key)
    if not recipe:
        return

    print(f"\nFound Recipe: {recipe.get('title', 'Unknown Title')}")
    recipe_id = recipe.get("id")
    
    # Get detailed recipe information
    detailed_recipe = get_recipe_information(recipe_id, api_key)
    if not detailed_recipe:
        return

    print("\nRecipe Details:")
    print("Title:", detailed_recipe.get("title", "N/A"))
    print("Ready in minutes:", detailed_recipe.get("readyInMinutes", "N/A"))
    print("Servings:", detailed_recipe.get("servings", "N/A"))
    
    print("\nIngredients:")
    for ingredient in detailed_recipe.get("extendedIngredients", []):
        print(" -", ingredient.get("original", ""))
    
    print("\nInstructions:")
    instructions = detailed_recipe.get("instructions")
    if instructions:
        print(instructions)
    else:
        print("No instructions available for this recipe.")

if __name__ == "__main__":
    main()

