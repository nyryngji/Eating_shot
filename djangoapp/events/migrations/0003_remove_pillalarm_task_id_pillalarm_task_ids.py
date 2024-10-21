# Generated by Django 5.1.2 on 2024-10-12 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_hospitalalarm_task_id_pillalarm_task_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pillalarm',
            name='task_id',
        ),
        migrations.AddField(
            model_name='pillalarm',
            name='task_ids',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]
