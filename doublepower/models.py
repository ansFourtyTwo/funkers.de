from django.db import models


class Player(models.Model):
    name = models.TextField(default='')
    forehand_strength = models.IntegerField(default=50)
    backhand_strength = models.IntegerField(default=50)
