# Generated by Django 4.2.7 on 2023-11-29 10:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("images", "0001_initial"),
        ("announcement", "0004_alter_announcement_images"),
    ]

    operations = [
        migrations.AlterField(
            model_name="announcement",
            name="images",
            field=models.ManyToManyField(blank=True, null=True, related_name="announcement", to="images.images"),
        ),
    ]
