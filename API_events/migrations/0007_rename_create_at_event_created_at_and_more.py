# Generated by Django 4.2.3 on 2023-07-09 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API_events', '0006_weatherevent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='countryOfEvent',
            new_name='event_country',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='dataOfEvent',
            new_name='event_date',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='idOfEvent',
            new_name='event_id',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='latOfEvent',
            new_name='event_lat',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='lonOfEvent',
            new_name='event_lon',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='nameOfEvent',
            new_name='event_name',
        ),
    ]