from project_v2 import get_city_data, get_number_of_iterations, temp_classification, prec_classification

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
    assert prec_classification(None) == "Missing precipitation data"#pytest for weather.py
