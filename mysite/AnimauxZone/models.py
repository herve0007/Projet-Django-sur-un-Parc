from django.db import models
from django.conf import settings


class ZoneCoeur(models.Model):
    nom=models.CharField(max_length=50)
    superficie=models.IntegerField()
    x=models.DecimalField(max_digits=15, decimal_places=2)
    y= models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        verbose_name="Zone Coeur"
        verbose_name_plural="Zone Coeurs"

    def __str__(self):
        return self.nom


class Animaux(models.Model):
    zoneCoeur=models.ForeignKey(ZoneCoeur, on_delete=models.CASCADE)
    espece=models.CharField(max_length=50)
    famille=models.CharField(max_length=50)
    texte=models.TextField()
    image=models.ImageField(upload_to='image/', blank=True)

    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animaux"

    def __str__(self):
        return self.espece
