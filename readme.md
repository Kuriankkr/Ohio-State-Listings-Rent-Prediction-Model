# **Ohio State Listings Rent Prediction Model**

## Overview
In the summer of 2020, I was planning to move from my current appartment and I started hunting online for appartment listings around Ohio State University. 
While googling, I noticed that multiple websites were putting up the same listing for different prices and I found this to be annoying. This little annoyment of mine made me think
as to how I wish, there existed a website where I could input my preferences and an accurate estimate of how much rent I should shell out would be predicted. Well! I decided to 
do it myself and this project therefore is the result of a small but significant issue that I thought I could and did resolve. I do believe the project has plenty of room for 
improvement and I shall address some of the issues below.

**The website can be accesed [here](https://ohio-state-listing-prediction.herokuapp.com/)**

The repository has been divided into 3 major sections:

- [Application](https://github.com/Kuriankkr/Ohio-State-Listings-Rent-Prediction-Model/tree/master/Application): This is the front end of the project that has been pushed to Heroku
- [Model](https://github.com/Kuriankkr/Ohio-State-Listings-Rent-Prediction-Model/tree/master/Model): This consists of the basic regression model that I have developed and an EDA
- [Scraping_Notebooks](https://github.com/Kuriankkr/Ohio-State-Listings-Rent-Prediction-Model/tree/master/Scraping_Notebooks): This consists for the notebooks that I used for scraping and the docker script

## Dataset
Since there was no preexisting clean datasets for appartments listings around Ohio State University, I had to scrape online from websites inorder to create my dataset.
I realized the most time consuming part of a Machine Learning project is getting the data and cleaning it up . The clean up included dealing with Null values, 
removing rows of data that didnt make sense, for example a house with 9 bedrooms and 1 bath would be an outlier and would affect the coefficients significantly.

The websites from which data were scrapped are given below:

- [Offcampus.osu.edu](https://offcampus.osu.edu/search-housing.aspx)
- [Appartments.com](https://www.apartments.com/off-campus-housing/oh/columbus/the-ohio-state-university/) 


The scrapping python files were dockerized for running them conviniently and are currently scheduled to run bi-weekly on airflow. The data is being stored on a postgres sql 
database.

Please [click here](https://github.com/Kuriankkr/Ohio-State-Listings-Rent-Prediction-Model/tree/master/Scraping_Notebooks) to view the notebooks.

## Evaluation
The evaluation metric that I used for this project was R-squared and standard error of regression. The reason I choose this metric has been discussed in my notebooks 
[here](https://github.com/Kuriankkr/Ohio-State-Listings-Rent-Prediction-Model/blob/master/Model/EDA%20and%20Regression%20Assumptions.ipynb)

My final R-squared value for my training set was **0.74** and testing was **0.72**. I believe this metric can be improved by the following methods:

- Making a robust model by scraping more websites
- Trying a weighted regression model with emphasis on coeffecients of location,beds and baths 
- Making the location feature more in-depth and specific, by mapping it with zipcodes
- Dealing with Null values in certain columns based on values for similar rows.

## Steps taken for implementation of the project

1) Create the web-scraping script for scrapping from multiple websites
2) Store the scrapped data into a postgres database.
3) Develop a Linear Regression model that learns from the data in the database.
4) Containerize the scripts using Docker.
5) Create a pipeline for automating steps 1 - 3.
6) Create the scripts for the front end of the project.
7) Deploy the webapp.

## Future Work

- **Front end**
  - Make the front end a lot more user-friendly and aesthitically pleasing
- **Model**
  - Insert more geographical features into the data to improve the prediction accuracy
  - Trying out out other prediction models such as a weighted regression model
- **Backend**
  - Scaling up the database to accomodate more data and thereby make the model more robust




# Future
