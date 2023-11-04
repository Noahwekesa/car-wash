from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    email = models.EmailField(unique=True)

GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
		('Null', 'not specified'),
    )
class Customer(models.Model):
	timestamp = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	email =  models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	typeofvehicle =  models.CharField(max_length=100)
	gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Null')
	location =  models.CharField(max_length=50)

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")