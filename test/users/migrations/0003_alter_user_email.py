# Generated by Django 4.2.7 on 2023-12-09 12:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_user_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name="email address"),
        ),
    ]
