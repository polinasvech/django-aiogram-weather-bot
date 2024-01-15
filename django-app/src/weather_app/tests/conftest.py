import pytest
from pytest_factoryboy import register
from weather_app.tests.factories import CityFactory

register(CityFactory)


@pytest.fixture()
def city(city_factory):
    return city_factory()
