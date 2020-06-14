from django.db import models
from django.urls import reverse


class Player(models.Model):
    name = models.TextField(default='')
    forehand_strength = models.IntegerField(default=50)
    backhand_strength = models.IntegerField(default=50)


class Team(models.Model):

    def get_absolute_url(self):
        return reverse('doublepower:view_team', args=[self.id])

    name = models.TextField(default='')
