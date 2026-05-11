from django.db import models

#makemigrations - create chang eand store in a file
#migrate - apply the pending change  created by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122) 
    email = models.CharField() 
    phone = models.CharField(max_length=12) 
    desc = models.TextField() 
    date = models.DateField() 

    def __str__(self):
        return self.name  

