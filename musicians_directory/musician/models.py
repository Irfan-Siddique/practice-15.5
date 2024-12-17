from django.db import models

# Create your models here.
class Musician(models.Model):
    firstName=models.CharField(max_length=20)
    lastName= models.CharField(max_length=20)
    email= models.EmailField()
    phoneNo= models.CharField(max_length=15)
    instrumentType=models.CharField(max_length=20)

    def __str__(self):
        return self.firstName