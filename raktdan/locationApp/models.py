from django.db import models

# Create your models here.
class Country(models.Model):
    country = models.CharField(max_length=100)
    country_code = models.CharField(max_length=4, default="+91")
    
    def __str__(self):
        return self.country

class State(models.Model):    
    country = models.ForeignKey(Country, related_name="StateCountry", on_delete=models.CASCADE)
    country_code = models.ForeignKey(Country, related_name="StateCountryCode",on_delete=models.CASCADE)
    state = models.CharField(max_length=100)
    def __str__(self):
        return self.state
    
class District(models.Model):
    country = models.ForeignKey(Country, related_name="DistrictCountry",on_delete=models.CASCADE)
    country_code = models.ForeignKey(Country, related_name="DistrictCountryCode",on_delete=models.CASCADE)
    state = models.ForeignKey(State, related_name="DistrictState",on_delete=models.CASCADE)
    district = models.CharField(max_length=100)
    def __str__(self):
        return self.district
