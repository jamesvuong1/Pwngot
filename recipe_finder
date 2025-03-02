<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Recipe Finder AI</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      max-width: 800px;
      margin: 2rem auto;
      padding: 1rem;
      line-height: 1.6;
    }
    h1, h2 {
      color: #333;
    }
    label {
      font-weight: bold;
    }
    input, button {
      padding: 0.5rem;
      font-size: 1rem;
      margin: 0.5rem 0;
      width: 100%;
      box-sizing: border-box;
    }
    #results {
      margin-top: 2rem;
      border-top: 1px solid #ccc;
      padding-top: 1rem;
    }
  </style>
</head>
<body>
  <h1>Recipe Finder AI</h1>
  <form id="recipe-form">
    <label for="ingredients">Enter Ingredients (comma-separated):</label>
    <input type="text" id="ingredients" name="ingredients" placeholder="e.g., chicken, tomato, basil" required>
    <button type="submit">Find Recipe</button>
  </form>

  <div id="results"></div>

  <script>
    // Hardcode your Spoonacular API key here
    const SPOONACULAR_API_KEY = "145f2f6c9b31454d9fdc12426fa6e04e";

    document.getElementById('recipe-form').addEventListener('submit', async function(event) {
      event.preventDefault();

      const ingredients = document.getElementById('ingredients').value.trim();
      const resultsDiv = document.getElementById('results');

      resultsDiv.innerHTML = '<p>Loading...</p>';

      try {
        // Build URL for the "find by ingredients" endpoint
        const findUrl = `https://api.spoonacular.com/recipes/findByIngredients?ingredients=${encodeURIComponent(ingredients)}&number=1&ranking=1&ignorePantry=true&apiKey=${SPOONACULAR_API_KEY}`;
        const findResponse = await fetch(findUrl);
        if (!findResponse.ok) {
          throw new Error(`Error fetching recipe: ${findResponse.statusText}`);
        }
        const recipes = await findResponse.json();

        if (recipes.length === 0) {
          resultsDiv.innerHTML = '<p>No recipes found for the provided ingredients.</p>';
          return;
        }

        const recipe = recipes[0];
        const recipeId = recipe.id;

        // Build URL for the detailed recipe information endpoint
        const infoUrl = `https://api.spoonacular.com/recipes/${recipeId}/information?apiKey=${SPOONACULAR_API_KEY}`;
        const infoResponse = await fetch(infoUrl);
        if (!infoResponse.ok) {
          throw new Error(`Error fetching recipe details: ${infoResponse.statusText}`);
        }
        const recipeDetails = await infoResponse.json();

        // Build the HTML to display recipe details
        let html = `<h2>${recipeDetails.title}</h2>`;
        html += `<p><strong>Ready in:</strong> ${recipeDetails.readyInMinutes} minutes</p>`;
        html += `<p><strong>Servings:</strong> ${recipeDetails.servings}</p>`;
        html += `<h3>Ingredients:</h3><ul>`;
        recipeDetails.extendedIngredients.forEach(ingredient => {
          html += `<li>${ingredient.original}</li>`;
        });
        html += `</ul>`;
        html += `<h3>Instructions:</h3>`;
        if (recipeDetails.instructions) {
          html += `<p>${recipeDetails.instructions}</p>`;
        } else {
          html += `<p>No instructions available.</p>`;
        }
        resultsDiv.innerHTML = html;
      } catch (error) {
        resultsDiv.innerHTML = `<p style="color: red;">Error: ${error.message}</p>`;
      }
    });
  </script>
</body>
</html>
