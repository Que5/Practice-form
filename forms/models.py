from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Form(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = PhoneNumberField()
    message = models.TextField()

    def __str__(self):
        return self.name
    
    
