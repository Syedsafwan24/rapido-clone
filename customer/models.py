from django.db import models

# Create your models here.
class User(models.Model):
    fullname = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    dob = models.DateField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    
    def __str__(self) -> str:
        return self.fullname
    
    
class DriverDetails(models.Model):
    # Personal Information
    fullname = models.CharField(max_length=100)
    dob = models.DateField()
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()

    # Identification
    license = models.CharField(max_length=20)
    vehicle_reg = models.CharField(max_length=20)

    # Bank Account Information
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=20)
    routing_number = models.CharField(max_length=20)

    # Vehicle Details
    vehicle_make = models.CharField(max_length=50)
    vehicle_model = models.CharField(max_length=50)
    vehicle_color = models.CharField(max_length=20)

    # Agreement
    agreement = models.BooleanField()

    def __str__(self):
        return self.fullname


class ContactQuery(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    USER_CHOICES = [
        ('Captain', 'Captain'),
        ('Customer', 'Customer'),
    ]
    user_type = models.CharField(max_length=8, choices=USER_CHOICES)
    query_type = models.CharField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return self.name

