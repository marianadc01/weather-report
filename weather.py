import re

class TemperatureConverter:

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9

    def celsius_to_fahrenheit(self, celsius):
        return celsius * 9/5 + 32

    def kelvin_to_celsius(self, kelvin):
        return kelvin - 273.15

    def celsius_to_kelvin(self, celsius):
        return celsius + 273.15
    
def main():
    unit = input("Choose temperature unit (C, F, K): ").upper()

    if unit not in ["C", "F", "K"]:
        print("Invalid temperature unit. Please choose C, F, or K.")
        return

    try:
        temperature = float(input("Enter the temperature: "))
    except ValueError:
        print("Invalid temperature value. Please enter a valid number.")
        return

    converter = TemperatureConverter()

    celsius = convert_temperature(unit, temperature, converter)

    classification = temp_classification(celsius)
    print(classification)

    display_emoji = display_temp(temperature, unit, celsius, converter)
    print(display_emoji)

def convert_temperature(unit, temperature, converter):
    if unit == "F":
        return converter.fahrenheit_to_celsius(temperature)
    elif unit == "K":
        return converter.kelvin_to_celsius(temperature)
    else:
        return temperature

def display_temp(original_temperature, unit, celsius, converter):
    fahrenheit = converter.celsius_to_fahrenheit(celsius)
    kelvin = converter.celsius_to_kelvin(celsius)
    
    return f"{original_temperature}{unit} is equal to {celsius:.2f}°C, {fahrenheit:.2f}°F, and {kelvin:.2f}K."

def temp_classification(celsius):
    emoji = ""
    if celsius < 0:
        classification = "Freezing temperatures!"
        emoji = "🥶"
    elif 0 <= celsius <= 10:
        classification = "Cold temperatures."
        emoji = "❄"
    elif 10 < celsius <= 20:
        classification = "Moderate temperatures."
        emoji = "😊"
    else:
        classification = "Hot temperatures!"
        emoji = "🥵"

    return f"{classification} {emoji}"

def rain_forecast(description):
    description = description.lower()
    if 'cloudy' in description or 'overcast' in description:
        return "It's going to be a cloudy day! 🌫️"
    elif 'clear' in description or 'sunny' in description:
        return "It's going to be a sunny day! ☀️"
    elif 'rain' in description or 'storm' in description:
        return "It's going to be a rainy day! ☔"
    else:
        return "Can you be more specific please?"

def word_count(description):
    word_count = re.findall(r"\b\W*um\b", description, re.IGNORECASE)
    return len(word_count)

if __name__ == "__main__":
   
    rain_description = input("Describe the sky: ")
    rain = rain_forecast(rain_description)
    print(rain)
    
    main()