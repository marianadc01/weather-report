# pip install pandas, pyarrow

"""import pandas as pd
df = pd.read_parquet('daily_weather.parquet')
new_df = df.to_csv('weather.csv')

# season, average temperatures 0.0, precipitation 0.0"""

import pandas as pd
import matplotlib.pyplot as plt

class TemperatureConverter:
    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9

    def celsius_to_fahrenheit(self, celsius):
        return celsius * 9/5 + 32

    def kelvin_to_celsius(self, kelvin):
        return kelvin - 273.15

    def celsius_to_kelvin(self, celsius):
        return celsius + 273.15


def temp_classification(celsius):
    emoji = ""
    if celsius < 0:
        classification = "Freezing temperatures!"
        emoji = "🥶"
    elif 0 <= celsius <= 10:
        classification = "Cold temperatures."
        emoji = "❄️"
    elif 10 < celsius <= 20:
        classification = "Moderate temperatures."
        emoji = "😊"
    else:
        classification = "Hot temperatures!"
        emoji = "🥵"

    return f"{classification} {emoji}"


def weather_analyzer(file_path, city_name, num_iterations=5):
    df = pd.read_parquet(file_path)

    # Filter data for the specified city
    city_df = df[df['city_name'] == city_name]

    if city_df.empty:
        print(f"No data found for the city {city_name}")
        return

    temp_converter = TemperatureConverter()

    dates = []
    avg_temps = []
    precipitations = []

    for _ in range(num_iterations):
        input_date = input("Enter a date (YYYY-MM-DD): ")
        selected_date = city_df[city_df['date'] == input_date]

        if not selected_date.empty:
            avg_temp = selected_date['avg_temp_c'].values[0]
            precipitation = selected_date['precipitation_mm'].values[0]

            celsius_temp = temp_converter.fahrenheit_to_celsius(avg_temp)
            classification = temp_classification(celsius_temp)

            print(f'Data for {input_date} in {city_name}:')
            print(f'Average Temperature: {avg_temp}°F ({celsius_temp:.2f}°C) {classification}')
            print(f'Precipitation: {precipitation}')

            dates.append(input_date)
            avg_temps.append(avg_temp)
            precipitations.append(precipitation)
        else:
            print(f"No data found for the date {input_date}")

    trend_df = pd.DataFrame({'Date': dates, 'Average Temperature': avg_temps, 'Precipitation': precipitations})

    plt.figure(figsize=(10, 6))
    plt.plot(trend_df['Date'], trend_df['Average Temperature'], label='Average Temperature', marker='o')
    plt.plot(trend_df['Date'], trend_df['Precipitation'], label='Precipitation', marker='o')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title(f'Temperature and Precipitation Trend in {city_name}')
    plt.legend()
    plt.show()


# Example usage
file_path = 'daily_weather.parquet'
city_name = input("Enter the city name: ")
weather_analyzer(file_path, city_name)

