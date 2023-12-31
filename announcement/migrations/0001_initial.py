# Generated by Django 4.2.7 on 2023-11-28 06:33

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("images", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Transports",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=50, unique=True)),
                (
                    "type",
                    models.CharField(
                        choices=[("BUS", "Avtobus"), ("METRO", "Metro"), ("MARSHUTKA", "Marshutka")], max_length=20
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Announcement",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=255)),
                ("partnership", models.BooleanField(default=False)),
                ("need_people_count", models.IntegerField(default=0)),
                ("room_count", models.IntegerField(default=1)),
                ("address", models.CharField(blank=True, max_length=255, null=True)),
                ("location_x", models.CharField(blank=True, max_length=255, null=True)),
                ("location_y", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "currency",
                    models.CharField(
                        choices=[("USD", "US Dollar"), ("EUR", "Euro"), ("UZS", "So`m")], default="UZS", max_length=10
                    ),
                ),
                ("total_price", models.FloatField(blank=True, null=True)),
                ("price_for_one", models.FloatField(blank=True, null=True)),
                ("appartment_status", models.IntegerField(validators=[django.core.validators.MaxValueValidator(10)])),
                ("description", models.TextField(blank=True, null=True)),
                ("conditioner", models.BooleanField(default=False)),
                ("washing_machine", models.BooleanField(default=False)),
                ("images", models.ManyToManyField(blank=True, null=True, to="images.images")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
