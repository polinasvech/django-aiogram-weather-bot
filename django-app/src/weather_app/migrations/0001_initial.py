from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="City",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=50, verbose_name="Название")),
                ("latitude", models.FloatField(verbose_name="Ширина")),
                ("longitude", models.FloatField(verbose_name="Долгота")),
                ("temperature", models.FloatField(blank=True, null=True, verbose_name="Температура, С")),
                ("pressure", models.FloatField(blank=True, null=True, verbose_name="Атмосферное давление, мм рт.ст.")),
                ("wind_speed", models.FloatField(blank=True, null=True, verbose_name="Скорость ветра, м/с")),
                ("updated_at", models.DateTimeField(auto_now=True, null=True, verbose_name="Обновлено")),
            ],
            options={
                "verbose_name": "Город",
                "verbose_name_plural": "Города",
                "ordering": ("-updated_at",),
            },
        ),
    ]
