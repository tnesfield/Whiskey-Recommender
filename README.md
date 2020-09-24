# The Whiskey Recommender



<p align="Left">
<img src="img/stag-antler-whiskey-flight.jpg" width="600" height="250">
</p>

Tehera Nesfield
[Github](https://github.com/tnesfield) | [Linked in](https://www.linkedin.com/in/tehera-nesfield/) |
<a href = "mailto: tehera.nesfield@gmail.com">Email</a>

# The Whiskey Flight Recommender 
## Discover Your New Favorite Whiskey


## Whiskey
* “Whiskey” is a Gaelic word which means “water of life.”
* Scottish and Canadian whiskies are spelled without the “e” and the others are spelled with it -- whiskey.
* The earliest known record of Whiskey production dates back to 1494.
* Jack Daniel’s was the best selling whiskey in the US in 2019.
* 37% of whiskey drinkers are women.
* True whiskey drinkers don't add ice.


## Data
I webscraped this dataset from <a href="https://www.whiskybase.com//">whiskeybase.com</a>, which has roughly 157,000 bottles. I chose this site because I was able to gather user ratings for each bottle of whiskey. I focused on popular whiskey distilleries and bottles that were in their core range. Meaning rare and limited bottles are not included. My dataset includes 4 types of whiskey - Scotch, Irish Bourbon and Japanese. There are 7 categories and 29 Distilleries.

## EDA
* I gathered 5125 ratings.
* The top 3 most frequently rated bottles are Scotch.
* Most reviewers gave 1 or 2 ratings, the most active reviewer gave 30 ratings.
* The average rating for bottles in my dataset is 85
* My lowest rating was 20 for a bottle of Irish Whiskey

<p align="left">
<img src="img/the_ratings.png" width="925" height="500">
</p>



## Model
The Whiskey Recommender uses explicit filtering. It takes a user’s whiskey type and budget and filters the dataset. It then uses matrix factorization using SVD in Surprise. My model was tested and received a RMSE score of 4.3.

<p align="left">
<img src="img/algorithm.png" width="400" height="400">
</p>

## Deployment

I deployed the recommender using Flask.

<p align="left">
<img src="img/website.png" width="400" height="400">
</p>

