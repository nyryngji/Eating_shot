# Generated by Django 5.1 on 2024-08-21 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='goal',
            field=models.CharField(blank=True, choices=[('chronic_disease', '만성질환'), ('healthy_diet', '건강한 식습관, 체중 감량')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='health_conditions',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]