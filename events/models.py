from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="Nom de l'événement",
        null=False,
        blank=False
    )
    asso = models.CharField(
        max_length=30,
        verbose_name="Asso organisatrice",
        null=False,
        blank=False
    )
    date = models.DateField(
        verbose_name="Date de l'évènement",
        null=False,
        blank=False
    )
    end_date = models.DateField(
        verbose_name="Date de fin de l'évènement",
        null=False,
        blank=True
    )
    description = models.CharField(
        max_length=2000,
        verbose_name="Description de l'événement",
        null=True,
        blank=False
    )
    image = models.CharField(
        max_length=1000,
        verbose_name="URL de la photo associée",
        null=True,
        blank=False
    )
    link = models.CharField(
        max_length=1000,
        verbose_name="Lien associé à l'évènement",
        null=True,
        blank=False
    )
    location = models.CharField(
        max_length=100,
        verbose_name="Lieu de l'évènement",
        null=True,
        blank=False
    )
    price = models.CharField(
        max_length=10,
        verbose_name="Prix de l'évènement",
        null=True,
        blank=False
    )
