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
    