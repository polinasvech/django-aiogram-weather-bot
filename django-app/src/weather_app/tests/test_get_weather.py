import pytest
from weather_app.services import CityNotFoundError, get_actual_weather


@pytest.mark.django_db
def test_get_actual_weather(city):
    temperature, pressure, wind_speed = get_actual_weather(city.name)

    assert temperature == city.temperature
    assert pressure == city.pressure
    assert wind_speed == city.wind_speed


@pytest.mark.django_db
def test_get_weather_city_not_found():
    city_name = "blabla"
    with pytest.raises(CityNotFoundError):
        _, _, _ = get_actual_weather(city_name)
