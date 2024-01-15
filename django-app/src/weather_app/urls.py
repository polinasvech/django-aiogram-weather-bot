from django.contrib import admin
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from weather_app.api.weather_view import get_weather

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("weather", get_weather),
]

urlpatterns = format_suffix_patterns(urlpatterns)
