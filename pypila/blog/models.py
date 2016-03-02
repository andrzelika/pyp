from django.db import models

class CzlonekRodziny(models.Model):
    imie = models.CharField(max_length=128)
    nazwisko = models.CharField(max_length=128)
    wiek = models.IntegerField()
