from django.contrib import admin
from weather_app.models import City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "temperature", "updated_at")
    readonly_fields = ("updated_at",)
