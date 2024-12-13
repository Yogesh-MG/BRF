from django.db import models

# Create your models here.


class Fillup(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(unique=True, blank=False)
    Service = models.CharField(max_length=100)
    Message = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.Name} -- {self.Email} -- {self.Service}"
    
class Newsletter(models.Model):
    Email = models.EmailField(blank=False, unique=True)
    
    def __str__(self):
        return f'{self.Email}'