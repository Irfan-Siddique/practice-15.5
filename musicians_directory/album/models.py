from django.db import models
from musician.models import Musician
# Create your models here.
class Album(models.Model):
    rating_choices={
        '1':'1',
        '2':'2',
        '3':'3',
        '4':'4',
        '5':'5',
    }
    albumName= models.CharField(max_length=50)
    musician= models.ForeignKey(Musician, on_delete=models.SET_NULL, null=True, blank=True)
    releaseDate=models.DateField()
    rating=models.CharField(max_length=20, choices=rating_choices)

    def __str__(self):
        return self.albumName
