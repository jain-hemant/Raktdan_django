from django.db import models

# Create your models here.
class BloodBank(models.Model):
    name = models.CharField(max_length=50)
    state = models.ForeignKey("locations.Model", verbose_name=_("state_area"), on_delete=models.CASCADE)
    district = models.ForeignKey("locations.Model", verbose_name=_("state_area"), on_delete=models.CASCADE)
    pin_code = models.IntegerField(max_length=6, min_length=6)