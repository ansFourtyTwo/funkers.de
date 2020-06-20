from django.db import models
from django.urls import reverse


class Player(models.Model):
    rank = models.PositiveIntegerField(default=1)
    name = models.TextField(default='')
    forehand_strength = models.IntegerField(default=50)
    backhand_strength = models.IntegerField(default=50)
    team = models.ForeignKey(
        'Team',
        on_delete=models.CASCADE,
        default=None
    )

    class Meta:
        ordering = ('rank',)


class Team(models.Model):

    def get_absolute_url(self):
        return reverse('doublepower:view_team', args=[self.id])

    name = models.TextField(default='')
