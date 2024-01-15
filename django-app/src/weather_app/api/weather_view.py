from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from weather_app.services import get_actual_weather


@api_view(["GET"])
def get_weather(request) -> Response:
    """
    Получение текущих значений температуры , атмосферного давления и скорости ветра в городе

    Обновление данных проводится в том случае, если прошло более 30 мин. с момента последнего запроса
    """
    city_name = request.GET.get("city").capitalize()
    temperature, pressure, wind_speed = get_actual_weather(city_name)

    return Response(
        {
            "name": city_name,
            "temperature": f"Температура {temperature}, С",
            "pressure": f"Атмосферное давление {pressure}, мм рт. ст.",
            "wind_speed": f"Скорость ветра {wind_speed}, м/c",
        }
    )
