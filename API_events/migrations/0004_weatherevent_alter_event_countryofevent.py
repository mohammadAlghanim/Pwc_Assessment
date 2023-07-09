# Generated by Django 4.2.3 on 2023-07-09 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API_events', '0003_event_countryofevent'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=64)),
                ('event_id', models.CharField(max_length=64)),
                ('event_Temperature', models.FloatField()),
                ('event_Humidity', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='countryOfEvent',
            field=models.CharField(max_length=64),
        ),
    ]