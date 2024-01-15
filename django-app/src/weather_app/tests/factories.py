import random
import factory
from django.utils.timezone import now
from faker import Factory as FakerFactory
from weather_app.models import City

faker = FakerFactory.create()


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = City

    name = factory.Faker("city")
    latitude = random.uniform(45, 55)
    longitude = random.uniform(35, 65)
    updated_at = factory.LazyAttribute(lambda x: now())

    temperature = random.uniform(-30, 30)
    pressure = random.uniform(700, 750)
    wind_speed = random.uniform(0, 20)
