# Generated by Django 4.2.6 on 2023-11-14 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PathCalculator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DroneFlightPath',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('flight_data_path', models.JSONField()),
                ('start', models.JSONField()),
                ('end', models.JSONField()),
                ('date_field', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
