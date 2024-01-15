import datetime as dt

from rest_framework.exceptions import NotFound
from weather_app.models import City


class CityNotFoundError(NotFound):
    default_detail = "Такого города нет в базе"

    def __init__(self, name):
        if name:
            self.detail = f"Такого города нет в базе: {name}"


def get_actual_weather(city_name: str) -> (float, float, float):
    """
    Обновляет данные о погоде, если в момента последнего запроса прошло > 30 мин.

    :param city_name: название города
    :return: информация о погоде в городе (температура, давление, скорость ветра)
    """
    try:
        city = City.objects.get(name=city_name)
    except City.DoesNotExist:
        raise CityNotFoundError(name=city_name)

    delta = dt.datetime.now() - city.updated_at.replace(tzinfo=None)
    print(int(delta.total_seconds() / 60))
    if int(delta.total_seconds() / 60) > 30:
        # Если с момента последнего обновления прошло более 30 минут,
        # обновляем данные о погоде
        city.update_weather()

    return city.temperature, city.pressure, city.wind_speed
