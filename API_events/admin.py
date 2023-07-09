from django.contrib import admin
from .models import Event,WeatherEvent,FlightList
# Register your models here.
admin.site.register(Event)
admin.site.register(WeatherEvent)
admin.site.register(FlightList)