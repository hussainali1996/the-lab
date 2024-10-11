from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass
    
    username = models.CharField(max_length=150, unique=True, blank=False)  
    email = models.EmailField(unique=True, blank=False)  
    phone_number = models.CharField(max_length=20, blank=False)  
    first_name = models.CharField(max_length=30, blank=True, null=False)   
    last_name = models.CharField(max_length=30, blank=True, null=False)   
            

    def __str__(self):
        return self.username
    
    def clean(self):
        
        pass