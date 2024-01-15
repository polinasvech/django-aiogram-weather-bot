import json
import os

import requests
from django.conf import settings
from django.db import models


class City(models.Model):
    """Модель города"""

    name = models.CharField(max_length=50, verbose_name="Название")
    latitude = models.FloatField(verbose_name="Ширина")
    longitude = models.FloatField(verbose_name="Долгота")
    temperature = models.FloatField(verbose_name="Температура, С", null=True, blank=True)
    pressure = models.FloatField(verbose_name="Атмосферное давление, мм рт.ст.", null=True, blank=True)
    wind_speed = models.FloatField(verbose_name="Скорость ветра, м/с", null=True, blank=True)
    updated_at = models.DateTimeField(verbose_name="Обновлено", auto_now=True, null=True)

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"
        ordering = ("-updated_at",)

    def __str__(self):
        return f"{self.name} ({self.latitude}, {self.longitude})"

    def update_weather(self):
        """
        Отправляет get-запрос к api яндекс.погоды и обновляет данные

        GET https://api.weather.yandex.ru/v2/forecast?lat=<широта>&lon=<долгота>
        """
        api_key = os.environ.get("API_KEY")
        weather = requests.get(
            f"https://api.weather.yandex.ru/v2/forecast?lat={self.latitude}&lon={self.longitude}",
            headers={"X-Yandex-API-Key": api_key},
        )
        resp = json.loads(weather.content)
        self.temperature = resp["fact"]["temp"]
        self.pressure = resp["fact"]["pressure_mm"]
        self.wind_speed = resp["fact"]["wind_speed"]
        self.save()
