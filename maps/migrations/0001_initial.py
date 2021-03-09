# Generated by Django 3.1.2 on 2021-03-09 12:11

from django.db import migrations, models
import mapbox_location_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserLocationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', mapbox_location_field.models.LocationField(map_attrs={})),
            ],
        ),
    ]
