# Analysing taste similarities in different cuisines

## Blog article
https://alioben.github.io/yummly/

# Abstract
Diets and food habits may vary widely from country to country in terms of ingredients and cooking techniques. Nevertheless, dishes from different regions may share similarities in flavours and tastes. This project aims to help people discover new recipes matching their preferences. Our analysis will be based on Yummly, a platform mainly used in North America containing recipes from different countries. First, we will characterise the taste preferences in a group of countries along with the nutritional intake of an average dish. Second, we will analyse similarities between cuisines in terms of flavours with the purpose of building a recipe recommender that matches one’s taste.

# How to run the Notebook
1. Clone the repository using `git clone <name repo>`
2. Download the dataset from [here](https://drive.google.com/open?id=18IHx-7FdWY9TdR4yHG2g-t1i0qAzdXOy) and unzip it under the folder data
3. Launch `jupyter notebook` and navigate to the cloned folder
4. Open `Final notebook.ipynb` to see the analysis

# Research questions
A list of research questions we would like to address during the project:
- What are the most commomly used ingredients?
- What are the most distinctive ingredients?
- How can we represent cuisines as a network of ingredients ?
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

# Task Distribution
- Ali Alami-Idrissi: Coming up with the algorithm, Crawling the data, Work on final presentation
- Ali Benlalah: Coding up the algorithm, Plotting graphs during data analysis, Work on final presentation
- Zakaria Fikrat: Writing up the report, Preliminary data analysis, Work on final presentation
