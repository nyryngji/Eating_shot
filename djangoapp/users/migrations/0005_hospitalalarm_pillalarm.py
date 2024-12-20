# Generated by Django 5.1.1 on 2024-10-07 08:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_alter_customuser_options_alter_customuser_managers_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="HospitalAlarm",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "hospital_name",
                    models.CharField(max_length=50),
                ),
                ("hospital_date", models.DateField()),
                ("hospital_time", models.TimeField()),
                ("is_active", models.BooleanField(default=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PillAlarm",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("pill_name", models.CharField(max_length=50)),
                ("weekday", models.CharField(max_length=50)),
                ("time", models.TimeField()),
                ("is_active", models.BooleanField(default=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
