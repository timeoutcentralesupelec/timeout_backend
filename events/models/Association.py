from django.db import models

class Association(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="Nom de l'association",
        blank=False
    )

    def __str__(self):
        return self.name