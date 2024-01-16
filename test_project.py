from project import get_city_data, get_number_of_iterations, temp_classification, prec_classification
from project import TemperatureConverter

def test_temp_classification():
    assert temp_classification(-10) == "Freezing temperatures! 🥶"
    assert temp_classification(10) == "Cold temperatures ❄️"
    assert temp_classification(15) == "Moderate temperatures 😊"
    assert temp_classification(25) == "Hot temperatures! 🥵"
    assert temp_classification(None) == "Missing temperature data"


def test_prec_classification():
    assert prec_classification(0.0) == "No rain ☀️"
    assert prec_classification(0.1) == "Light rain ☂️"
    assert prec_classification(7.5) == "Moderate rain 🌧️"
    assert prec_classification(10.0) == "Heavy rain! 🌧️🌧️"
    assert prec_classification(None) == "Missing precipitation data"

def test_get_date():
    assert get_date(31-12-2000) == "Invalid date format. Please use YYYY-MM-DD."
    assert get_date(12-31-2000) == "Invalid date format. Please use YYYY-MM-DD."
    assert get_date(2000-12-32) == "Invalid date. Please try again."


# test the functions inside the class TemperatureConverter
converter = TemperatureConverter()

def test_C_to_F():
    assert converter.celsius_to_fahrenheit(0) == 32
    assert converter.celsius_to_fahrenheit(-10) == 14
    assert converter.celsius_to_fahrenheit(100) == 212    


def test_C_to_K():
    assert converter.celsius_to_kelvin(0) == 273.15
    assert converter.celsius_to_kelvin(-273.15) == 0 
    assert converter.celsius_to_kelvin(100) == 373.15   
