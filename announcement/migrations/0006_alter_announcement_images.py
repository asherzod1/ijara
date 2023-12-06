# Generated by Django 4.2.7 on 2023-11-29 10:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("images", "0001_initial"),
        ("announcement", "0005_alter_announcement_images"),
    ]

    operations = [
        migrations.AlterField(
            model_name="announcement",
            name="images",
            field=models.ManyToManyField(related_name="announcement", to="images.images"),
        ),
    ]
