# Analysing taste similarities in different cuisines

# Abstract
Diets and food habits may vary widely from country to country in terms of ingredients and cooking techniques. Nevertheless, dishes from different regions may share similarities in flavours and tastes. This project aims to help people discover new recipes matching their preferences. Our analysis will be based on Yummly, a platform mainly used in North America containing recipes from different countries. First, we will characterise the taste preferences in a group of countries along with the nutritional intake of an average dish. Second, we will analyse similarities between cuisines in terms of flavours with the purpose of building a recipe recommender that matches one’s taste.

# Research questions
A list of research questions we would like to address during the project:
- What are the taste preferences of each country?
- How can we define a country’s taste preferences in term of ingredients?
- What are the different clusters of countries sharing similar tastes?
- What measure of similarity can we use to suggest a similar cuisine?
- What are the nutritional intakes of a typical dish in a country?
- Does it correlate with the country’s taste preferences?

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

We built a scrapper `spider.py` to collect recipes from a number of cuisines with the Yummly API.The results can be found under the `data` folder.
Here is a sample of a search recipe result:


Each recipe has an id which we use to get more data about the recipe (nutrition facts, cooking time, etc …).
Here is a sample of the result we get using the search with id:


# A list of internal milestones up until project milestone 2
We setup the following goals as next milestones:
- Retrieve a raw dataset by crawling the Yummly website and/or API
- Clean the dataset and perform a first exploratory analysis
- Characterise the metrics used to measure the taste preferences (salty/sweet…)

# Questions for TAa
None.
