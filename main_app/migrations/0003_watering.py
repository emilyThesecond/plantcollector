# Generated by Django 5.0.1 on 2024-01-11 19:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_plant_delete_cat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('method', models.CharField(choices=[('T', 'Top-Watering'), ('B', 'Bottom-Watering')], default='T', max_length=1)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.plant')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
