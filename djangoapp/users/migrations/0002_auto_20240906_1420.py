# Generated by Django 5.1.1 on 2024-09-06 05:20

from django.db import migrations


def populate_exercise_types(apps, schema_editor):
    ExerciseType = apps.get_model("users", "ExerciseType")
    exercise_types = [
        ("tennis_duals", 330, "테니스(복식)"),
        ("water_skiiing", 440, "수상스키"),
        ("general_stretching", 180, "체조"),
        ("walking5point6kmh", 270, "걷기(5.6km/h)"),
        ("general_aerobics", 330, "에어로빅"),
        ("tennis_singles", 440, "테니스(단식)"),
        ("swimming", 720, "수영"),
        ("golf", 270, "골프"),
        ("skiiing", 540, "스키"),
        ("hiking", 780, "등산"),
        ("bicycling9point7kmh", 270, "자전거(9.7km/h)"),
        ("skating6point4kmh", 390, "스케이팅(6.4km/h)"),
        ("bowling", 270, "볼링"),
        ("bicycling16kmh", 390, "자전거(16km/h)"),
        ("running9kmh", 630, "달리기(9km/h)"),
        ("table_tennis", 330, "탁구"),
        ("taking_steps", 310, "계단 오르내리기"),
        ("badminton", 330, "배드민턴"),
        ("volleyball", 330, "배구"),
    ]

    for exercise_type in exercise_types:
        ExerciseType.objects.create(
            name=exercise_type[2], calories_per_hour=exercise_type[1]
        )


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(populate_exercise_types),
    ]
