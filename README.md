# iPython Final Project - Weather Report                        
### Created by: Maria Dolgaya (28168) and Mariana Coelho (25605)  
### Professor Manuel Lameiras de Figueiredo Campagnolo            
### MSc in Green Data Science, ISA, Portugal 

For our final project for the class Introduction to Python, we have decided to create a code to provide the user with a weather report for almost any city in the world in any date of choice, and in the end, it give a prediction plot graph.

The data set that was chosen to implement in this project was obtained in keggle and it's called [The Weather Dataset](https://www.kaggle.com/datasets/guillemservera/global-daily-climate-data/data). This dataset was created by Guillem Servera and was updated weekly usisng data from Meteostat API, until four months ago when this stop. Therefore, the user is restricted to only access weather data until August of 2023.

The code used to obtain the data report contains six functions plus the main one. The six functions are: a function to get the city weather data from the .parquet file from the dataset; a function to establish the number of dates the user can obtain information about (so far, it's limited to five); a function to get the specifc dates on which the user wants to collect information about; a function that specifies the temperature (very cold, kind of warn, etc) based on the temperature provided and it returns with emojies based on the temperture classification; a function similar to the previous onebut for precipitation; and finally, a function to create a plot graph showing the weather trend based on those five specifct dates.

Besides these functions, we also implemented a class to convert tempertures provided in Celsius degrees in temperatures in both Kelvin and Fahrenheit degrees.

This project also includes another Python file, called test_project, with the test functions, to make sure the code works properly, as well as a text file, called requeriments, with all the Python packges needed for the code to work.





