from django.db import models

# Create your models here.
class UserModel(models.Model):
    BLOOD_GROUP = [("A+","A+"),("B+","B+"),("AB+","AB+"),("O+","O+")]
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    blood = models.CharField(max_length=3,choices=BLOOD_GROUP)
    phone = models.CharField(max_length=10)
    phone2 = models.CharField(max_length=10, null = True)
    address = models.CharField(max_length=100)
    createdDate = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.firstName} {self.lastName} {self.blood}"

