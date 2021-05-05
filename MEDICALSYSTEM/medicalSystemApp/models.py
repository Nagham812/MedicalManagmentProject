from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10)
    email = models.EmailField(default='')
    phone = models.CharField(max_length=17)
    dateOfBirth = models.DateField()
    speciality = models.CharField(max_length=20)
    #working shift


class Patient(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10)
    email = models.EmailField(default='')
    phone = models.CharField(max_length=17)
    city = models.CharField(max_length=20)
    dateOfBirth = models.DateField()
    height = models.FloatField()
    weight = models.FloatField()
    #List of Cronec Disases
    #Insurance Info
    #history
