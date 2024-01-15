from django.core.management.base import BaseCommand, CommandError
from weather_app.models import City


class Command(BaseCommand):
    help = "Create City objects from cities.txt"

    def handle(self, *args, **options):
        cities_file = open("weather_app/cities.txt", "r")
        for line in cities_file.readlines():
            line = line.strip()
            if len(line) > 1:
                city_info = [s.strip() for s in line.split("—")]

                try:
                    City.objects.get(name=city_info[0])
                except City.DoesNotExist:
                    coords = [s.strip() for s in city_info[1].split(",")]
                    city = City(name=city_info[0], latitude=coords[0], longitude=coords[1])
                    city.save()
                    continue
