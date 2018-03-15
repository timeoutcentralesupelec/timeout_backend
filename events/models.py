from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Event(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="Nom de l'événement",
        blank=False
    )
    asso = models.CharField(
        max_length=30,
        verbose_name="Asso organisatrice",
        blank=False
    )
    date = models.DateTimeField(
        verbose_name="Date de l'évènement",
        null=False,
        blank=False
    )
    end_date = models.DateTimeField(
        verbose_name="Date de fin de l'évènement",
        null=False,
        blank=False,
    )
    description = RichTextField(
        max_length=2000,
        verbose_name="Description de l'événement",
        blank=True,
    )
    image = models.CharField(
        max_length=1000,
        verbose_name="URL de la photo associée",
        blank=False
    )
    link = models.CharField(
        max_length=1000,
        verbose_name="Lien associé à l'évènement",
        blank=True
    )
    location = models.CharField(
        max_length=100,
        verbose_name="Lieu de l'évènement",
        blank=False
    )
    price = models.CharField(
        max_length=10,
        verbose_name="Prix de l'évènement",
        blank=False
    )

    def __str__(self):
        return self.name
