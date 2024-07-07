from django.db import models
from locationApp.models import State,Country,District

# Create your models here.

class HospitalDetail(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True,null=True)
    contact = models.CharField(max_length=10)
    website = models.URLField(null = True)
    country = models.ForeignKey(Country,related_name="HospitalDetails",on_delete=models.CASCADE)
    state = models.ForeignKey(State,related_name="HospitalDetails",on_delete=models.CASCADE)
    district = models.ForeignKey(District,related_name="HospitalDetails",on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    pin = models.CharField(max_length=6)
    latitude = models.FloatField()
    longitude = models.FloatField()



