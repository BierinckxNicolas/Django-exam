

from django.db import models


class Infraction(models.Model):
    street = models.CharField(max_length=200)
    speed_limit = models.IntegerField
    infraction_speed = models.IntegerField

    def __str__(self):
        return self.street
    
    
