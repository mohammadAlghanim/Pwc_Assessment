# Generated by Django 4.2.3 on 2023-07-09 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API_events', '0002_alter_event_create_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='countryOfEvent',
            field=models.CharField(default='peaky', max_length=64),
        ),
    ]
