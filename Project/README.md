# Analysing taste similarities in different cuisines

# Abstract
Diets and food habits may vary widely from country to country in terms of ingredients and cooking techniques. Nevertheless, dishes from different regions may share similarities in flavours and tastes. This project aims to help people discover new recipes matching their preferences. Our analysis will be based on Yummly, a platform mainly used in North America containing recipes from different countries. First, we will characterise the taste preferences in a group of countries along with the nutritional intake of an average dish. Second, we will analyse similarities between cuisines in terms of flavours with the purpose of building a recipe recommender that matches one’s taste.

# Research questions
A list of research questions we would like to address during the project:
- What are the most commomly used ingredients?
- What are the most distinctive ingredients?
- How can we cluster cuisine in terms of their recipe components?
- How do cuisines influence each other?

# Dataset
Yummly provides an API (https://developer.yummly.com/intro) with a limited number of calls for academic projects. We already sent a request to get access to it. The limit is set to 30K calls in total, therefore we may need to build a web crawler to scrap the data.
Yummly’s platform provides a search engine which filters the recipes by cuisine origin (e.g. Japanese, Italian…) and flavours (e.g. sweet, salty…). For each recipe, Yummly provides its ingredients, nutritional facts and some tags characterising the dish.
The Yummly API provides  the following endpoints for searching and fetching recipes:
- `GET` requests can be done in the following way: `http://api.yummly.com/v1/api/recipes?_app_id=app-id&_app_key=app-key&your _search_parameters` to search recipes
- The parameter `allowedCuisine[]` filter the search results based a specific cuisine
- The parameters `salty`, `sour`, `sweet`, `bitter`, `meaty` and `piquant` specify the expected taste of the results
- The API returns JSON objects containing information about the recipes matching the query argument
In the case where Yummly limits our usage of the API, we will build a web crawler based on the following pattern in the website’s HTML DOC and URLs:
- The search URLs are structured in the following way: `https://www.yummly.com/recipes?q=search_parameters`
- The search parameters passed in the URL search query are similar to the ones described in the API documentation
- The returned HTML contains links to recipes information pages nested in div tags having the same class attribute
- The recipes information pages have also the same pattern and can be web scrapped using the techniques studied in the course 

## UPDATE:

We built a scrapper `spider.py` to collect recipes from a number of cuisines with the Yummly API. For each of the following cuisines: `American, Chinese, Cuban, English, French, German, Greek, Hawaiian, Hungarian, Indian, Irish, Italian, Japanese, Mexican, Moroccan, Portuguese, Spanish, Swedish, Thai`, we access the first 500 results using the search endpoint (see above), and save them in json files. The results can be found under the `data` folder.
Here is a sample of a search recipe result:
```json
{
	"attributes": {
	    "course": [
	        "Soups"
	    ],
	    "cuisine": [
	        "Italian"
	    ]
	},
	"flavors": {
	    "salty": 0.6666666666666666,
	    "sour": 0.8333333333333334,
	    "sweet": 0.6666666666666666,
	    "bitter": 0.5,
	    "meaty": 0.16666666666666666,
	    "piquant": 0.5
	},
	"rating": 4.6,
	"id": "Vegetarian-Cabbage-Soup-Recipezaar",
	"smallImageUrls": [],
	"sourceDisplayName": "Food.com",
	"totalTimeInSeconds": 4500,
	"ingredients": [
	    "garlic cloves",
	    "ground pepper",
	    "diced tomatoes",
	    "celery",
	    "tomato juice",
	    "salt",
	    "cabbage",
	    "bell peppers",
	    "oregano",
	    "carrots",
	    "basil",
	    "vegetable broth",
	    "chili pepper flakes",
	    "green beans",
	    "onions",
	    "onion soup mix"
	],
	"recipeName": "Vegetarian Cabbage Soup"
}
```

Each recipe has an `id` which can be used to get more data about the recipe (nutrition facts, cooking time, etc …).
Here is a sample of a recipe:
```json
{
    "attribution": {
        "html": "<a href='http://www.yummly.com/recipe/Hot-Turkey-Salad-Sandwiches-Allrecipes'>Hot Turkey Salad Sandwiches recipe</a> information powered by <img src='http://static.yummly.com/api-logo.png'/>",
        "url": "http://www.yummly.com/recipe/Hot-Turkey-Salad-Sandwiches-Allrecipes",
        "text": "Hot Turkey Salad Sandwiches recipes: information powered by Yummly",
        "logo": "http://static.yummly.com/api-logo.png"
    },
    "ingredientLines": [
        "2 cups diced cooked turkey",
        "2 celery ribs, diced",
        "1 small onion, diced",
        "2 hard-cooked eggs, chopped",
        "3/4 cup mayonnaise",
        "1/2 teaspoon salt",
        "1/4 teaspoon pepper",
        "6 hamburger buns, split"
    ],
    "flavors": {
        "Salty": 0.004261637106537819,
        "Meaty": 0.0019220244139432907,
        "Piquant": 0,
        "Bitter": 0.006931612268090248,
        "Sour": 0.009972159750759602,
        "Sweet": 0.0032512755133211613
    },
    "nutritionEstimates": [
        {
            "attribute": "SUGAR",
            "description": "Sugars, total",
            "value": 5.25,
            "unit": {
                "name": "gram",
                "abbreviation": "g",
                "plural": "grams",
                "pluralAbbreviation": "grams"
            }
        },
        {
            "attribute": "PROCNT",
            "description": "Protein",
            "value": 17.6,
            "unit": {
                "name": "gram",
                "abbreviation": "g",
                "plural": "grams",
                "pluralAbbreviation": "grams"
            }
        },
        {
            "attribute": "VITA_IU",
            "description": "Vitamin A, IU",
            "value": 159.13,
            "unit": {
                "name": "IU",
                "abbreviation": "IU",
                "plural": "IU",
                "pluralAbbreviation": "IU"
            }
        },
        {
            "attribute": "VITC",
            "description": "Vitamin C, total ascorbic acid",
            "value": 0,
            "unit": {
                "name": "gram",
                "abbreviation": "g",
                "plural": "grams",
                "pluralAbbreviation": "grams"
            }
        },
        {
            "attribute": "CA",
            "description": "Calcium, Ca",
            "value": 0.08,
            "unit": {
                "name": "gram",
                "abbreviation": "g",
                "plural": "grams",
                "pluralAbbreviation": "grams"
            }
        },
        {
            "attribute": "FE",
            "description": "Iron, Fe",
            "value": 0,
            "unit": {
                "name": "gram",
                "abbreviation": "g",
                "plural": "grams",
                "pluralAbbreviation": "grams"
            }
        }
    ],
    "images": [
        {
            "hostedLargeUrl": "http://i2.yummly.com/Hot-Turkey-Salad-Sandwiches-Allrecipes.l.png",
            "hostedSmallUrl": "http://i2.yummly.com/Hot-Turkey-Salad-Sandwiches-Allrecipes.s.png"
        }
    ],
    "name": "Hot Turkey Salad Sandwiches",
    "yield": "6 servings",
    "totalTime": "30 Min",
    "attributes": {
        "holiday": [
            "Christmas",
            "Thanksgiving"
        ],
        "cuisine": [
            "Italian",
            "Soul food",
            "American"
        ]
    },
    "totalTimeInSeconds": 1800,
    "rating": 4.44,
    "numberOfServings": 6,
    "source": {
        "sourceRecipeUrl": "http://allrecipes.com/Recipe/hot-turkey-salad-sandwiches/detail.aspx",
        "sourceSiteUrl": "http://www.allrecipes.com",
        "sourceDisplayName": "AllRecipes"
    },
    "id": "Hot-Turkey-Salad-Sandwiches-Allrecipes"
}
```
For the purpose of our project, we are interested in flavours, ingredients and nutritional facts of recipe from different cuisines which we successfully collected using the steps above.

# A list of internal milestones up until project milestone 2
We setup the following goals as next milestones:
- Retrieve a raw dataset by crawling the Yummly website and/or API
- Clean the dataset and perform a first exploratory analysis
- Characterise the metrics used to measure the taste preferences (salty/sweet…)

# Questions for TAa
None.
