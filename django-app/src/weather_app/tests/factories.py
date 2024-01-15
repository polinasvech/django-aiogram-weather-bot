# tests/factories.py

from datetime import timezone

import factory
from django.contrib.auth.models import User
from django.utils.timezone import now
from faker import Factory as FakerFactory
from faker import Faker
from weather_app.models import City

faker = FakerFactory.create()


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = City

    name = factory.Faker("city")
    latitude = 55.15
    longitude = 61.43
    updated_at = factory.LazyAttribute(lambda x: now())

    temperature = -18.0
    pressure = 726.0
    wind_speed = 1.9
    # email = factory.Faker("safe_email")
    # username = factory.LazyAttribute(lambda x: faker.name())


#     @classmethod
#     def _prepare(cls, create, **kwargs):
#         password = kwargs.pop("password", None)
#         user = super(UserFactory, cls)._prepare(create, **kwargs)
#         if password:
#             user.set_password(password)
#             if create:
#                 user.save()
#         return user
#
#
# class GameFactory(factory.django.DjangoModelFactory):
#     room_name = factory.LazyAttribute(lambda x: faker.name())
#     game_status = "active"
#     created_at = factory.LazyAttribute(lambda x: now())
#     updated_at = factory.LazyAttribute(lambda x: now())
#     round_started = False
#     is_joinable = True
#
#     class Meta:
#         model = Game
#
#
# class GamePlayerFactory(factory.django.DjangoModelFactory):
#     followers = 0
#     selfies = 3
#     user = factory.SubFactory(UserFactory)
#     started = False
#     game = factory.SubFactory(GameFactory)
#
#     class Meta:
#         model = GamePlayer
#
#
# class MessageFactory(factory.django.DjangoModelFactory):
#     game = factory.SubFactory(GameFactory)
#     username = None
#     message = factory.LazyAttribute(lambda x: faker.sentence())
#     created_at = factory.LazyAttribute(lambda x: now())
#     message_type = None
#
#     class Meta:
#         model = Message
