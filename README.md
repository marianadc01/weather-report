# iPython Final Project - Weather Report                        
### Created by: Maria Dolgaya (28168) and Mariana Coelho (25605)  
### Professor Manuel Lameiras de Figueiredo Campagnolo            
### MSc in Green Data Science, ISA, Portugal 

For our final project for the class Introduction to Python, we have decided to create a code to provide the user with a weather report for almost any city in the world in any date of choice, and in the end, it gives a trend plot graph.

The data set that was chosen to implement in this project was obtained in Kaggle and it's called [The Weather Dataset](https://www.kaggle.com/datasets/guillemservera/global-daily-climate-data/data). The data obtained can be found in the daily_weather.parquet file, which needs to be downloaded from Kaggle, extracted from a zip file and put in the same place as the code is being stored so the code can access it. This dataset was created by Guillem Servera and contains weather reports form several cities dating all the way back to January 2nd, 1833. The dataset was updated weekly usisng data from Meteostat API, until four months ago when this stopped, therefore the user is restricted to only access weather data until August of 2023. There's also some limitations with the cities to chose, so it's advised that the user see the cities.csv file (also from the Kaggle dataset) to know whih cities are available for analysis.

The code used to obtain the data report contains six functions plus the main one. The six functions are: 
- get_city(): a function to get the city weather data from the .parquet file from the dataset;
- get_number_of_inerations(): a function to establish the number of dates the user can obtain information about;
- get_date(): a function to get the specifc dates on which the user wants to collect information about;
- temp_classification(): a function that specifies the temperature (very cold, kind of warn, etc) based on the temperature provided and it returns with emojies based on the temperture classification;
- prec_classification(): a function similar to the previous one but for precipitation;
- and finally, plot_weather_trend(): a function to create a plot graph showing the weather trend based on those five specific dates.

Besides these functions, we also implemented a class, class TemperatureConverter, to convert tempertures provided in Celsius degrees in temperatures in both Kelvin and Fahrenheit degrees. 

The main function calls all mentioned ones and the class as well as checks if the dataset contains any values for the user's input date.   

This project also includes another Python file, called test_project, with the following test functions: 
- test_temp_classification(): to check if the temperature classificationfunction works properly; 
- test_prec_classification(): to do the same for the precipitation classification; 
- test_C_to_F: to test preciseness of Celsius-Farenheit convertion (class TemperatureConverter);
- test_C_to_K: to test preciseness of Celsius-Kelvin convertion (class TemperatureConverter).

And lastly, the project includes a text file, called requirements, with all the Python packges needed for the code to be used.





