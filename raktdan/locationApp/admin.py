from django.contrib import admin
from .models import Country, State, District
# Register your models here.
admin.site.register(Country)
admin.site.register(State)
admin.site.register(District)