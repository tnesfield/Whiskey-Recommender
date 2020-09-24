# The Whiskey Recommender



<p align="Left">
<img src="img/stag-antler-whiskey-flight.jpg" width="800" height="200">
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
I gathered 5125 ratings.
The top 3 most frequently rated bottles are Scotch.
Most reviewers gave 1 or 2 ratings, the most active reviewer gave 30 ratings.
The average rating for bottles in my dataset is 85
My lowest rating was 20 for a bottle of Irish Whiskey

<p align="left">
<img src="img/the_ratings.png" width="200" height="400">
</p>

<iframe src='https://gfycat.com/ifr/BowedEvilGaur' frameborder='0' scrolling='no' allowfullscreen width='640' height='1182'></iframe>


## Goal
Accurately classify a given image from a dataset into different disease categories or a healthy leaf.

<p align="center">
<img src="graphics/tomato_leaves.png" width="850" height="450">
</p>

## Dataset
My dataset was a little imbalanced. Total images = 12,814

<a href="https://github.com/spMohanty/PlantVillage-Dataset/tree/master/raw/color">
<p align="center">
<img src="graphics/pie_chart.png" width="800" height="450">
</a>

## Model Framework
I used a keras Sequential model with 9 layers

<p align="left">
<img src="graphics/model.png" width="200" height="400">
</p>

## Results

* My train set ran with **96% accuracy**
* My validation set ran with **93% accuracy**
* My holdout set ran with **92% accuracy**

<p align="left">
<img src="graphics/training-test-accuracy.png" width="350" height="350">
</p>
<p align="left">
<img src="graphics/training-results.png" width="400" height="100">
</p>
                                                               
### Confusion Matrix

<p align="center">
<img src="graphics/confusion-matrix.png" width="850" height="700">
</p>
