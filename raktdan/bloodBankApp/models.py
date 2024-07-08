from django.db import models
from locationApp.models import Country, State, District
from django.core.validators import RegexValidator

# Create your models here.
class BloodBank(models.Model):    
    bankName = models.CharField(max_length=50)
    bank_contact = models.CharField(
        verbose_name='Mobile Number',
        max_length=10,
        validators=[RegexValidator(r'^\d{10}$', 'Mobile number must be exactly 10 digits.')],
        help_text='Enter a 10-digit mobile number',
        null=True,
        blank=True
    )
    bankCountry = models.ForeignKey(Country, related_name='bloodBanks',on_delete=models.CASCADE)
    bankState = models.ForeignKey(State, related_name='bloodBanks', on_delete=models.CASCADE)
    bankDistrict = models.ForeignKey(District, related_name='bloodBanks', on_delete=models.CASCADE)
    bankPincode = models.CharField(
        verbose_name='Pin Code',
        max_length=6,
        validators=[RegexValidator(r'^\d{6}$', 'Mobile number must be exactly 6 digits.')],
        help_text='Enter a 6-digit area PinCode'
    )
    
    def __str__(self) -> str:
        return f"{self.bankName}-{self.bankState}-{self.bankDistrict}"


class BloodDonor(models.Model):
    BLOOD_GROUP_CHOICES = [
        ('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')
    ]
    RH_FACTOR_CHOICES = [
        ('+', '+'), ('-', '-')
    ]
    donorName = models.CharField(max_length=50)
    mobile_number = models.CharField(
        verbose_name='Mobile Number',
        max_length=10,
        validators=[RegexValidator(r'^\d{10}$', 'Mobile number must be exactly 10 digits.')],
        help_text='Enter a 10-digit mobile number',
        null=True,
        blank=True
    )
    donorEmail = models.EmailField(null=True)
    donorCountry = models.ForeignKey(Country, related_name='bloodDonors',on_delete=models.CASCADE)
    donorState = models.ForeignKey(State, related_name='bloodDonors', on_delete=models.CASCADE)
    donorDistrict = models.ForeignKey(District, related_name='bloodDonors', on_delete=models.CASCADE)
    donorPincode = models.CharField(
        verbose_name='Pin Code',
        max_length=6,
        validators=[RegexValidator(r'^\d{6}$', 'Mobile number must be exactly 6 digits.')],
        help_text='Enter a 6-digit area PinCode'
    )
    donorBloodGroup = models.CharField(max_length=5, choices = BLOOD_GROUP_CHOICES)
    donorRhFactor = models.CharField(max_length=5, choices = RH_FACTOR_CHOICES)

    def __str__(self) -> str:
        return f"{self.donorName}-{self.donorBloodGroup}{self.donorRhFactor}-{self.donorState}-{self.donorDistrict}"
    
class BloodStock(models.Model):
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O+', 'O+'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-'), ('O-', 'O-')
    ]
    bloodGroup = models.CharField(max_length=5, choices=BLOOD_GROUP_CHOICES)
    stock = models.PositiveIntegerField(default=0)
    
    def __str__(self) -> str:
        return f"Blood Group: {self.bloodGroup} | Stock: {self.stock}"