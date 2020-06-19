from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Player


@receiver(pre_save, sender=Player)
def auto_set_ranking(sender, instance, **kwargs):
    # If instance is not yet saved to the DB, it will not have set a
    # private key, thus we can initialize the player's rank
    if instance.pk is None:
        instance.rank = len(instance.team.player_set.all()) + 1
