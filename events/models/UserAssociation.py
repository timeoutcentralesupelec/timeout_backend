from django.db import models
from django.contrib.auth.models import User
from events.models.Association import Association


class UserAssociation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.ForeignKey(Association,on_delete=models.CASCADE)