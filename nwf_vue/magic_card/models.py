from django.db import models
from django.contrib.auth.models import User
from game.models import Game
# Create your models here.
class MagicCard(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='submissions', null=True, blank=True)
    round_submitted = models.IntegerField()
    chosen = models.BooleanField(default=False)
    card_name = models.CharField(max_length=1000)
    submitted = models.BooleanField(default=False)
    card_color = models.CharField(
        max_length = 15
        )
    card_type = models.CharField(
        max_length = 256
    )
    converted_mana_cost = models.CharField(max_length=240)
    card_text = models.TextField()
    flavor_text = models.TextField()
