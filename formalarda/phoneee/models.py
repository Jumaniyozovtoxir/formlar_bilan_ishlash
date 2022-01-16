from django.db import models

# Create your models here.
class Telefon(models.Model):
    brand = models.CharField(max_length=700)
    nomi = models.CharField(max_length=700)
    xotira= models.IntegerField()
    rangi = models.CharField(max_length=70)
    narxi = models.CharField(max_length=70)

    def __str__(self):
        return self.nomi

