from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Game(models.Model):
    start = models.BooleanField(default=False)
    in_progress = models.BooleanField(default=False)
    judging = models.IntegerField(default=0)
    round = models.IntegerField(default=1)
    number_of_players = models.IntegerField()
    number_of_rounds = models.IntegerField()
    players = models.ManyToManyField(User, through='InGame')
    card_name = models.CharField(max_length=1000)
    completed = models.BooleanField(default = False)
    judge = models.CharField(max_length = 256, blank=True)
    name = models.CharField(max_length=300),
    number_of_submissions = models.IntegerField(default=0)

    #Select a random magic card name to use as the game name
    def game_name(self):
        with open(WORDS_DIR + '/cards.txt') as f:
            cards = f.read().splitlines()
            card = random.choice(cards)
        return card

    #Notify players when a game starts, a card is submitted, or when a game has ended
    def notify_players(self, subject, message):
        recipient_list = [str(player.username) for player in self.players]

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            recipient_list,
            )

    #Create the card name
    def get_card_name(self):

        with open(WORDS_DIR + "/names.txt") as f:
            name = random.choice(f.read().splitlines())
        f.close()

        with open(WORDS_DIR + '/adverbs.txt') as f:
           advb = random.choice(f.read().splitlines())
        f.close()

        with open(WORDS_DIR + '/nouns.txt') as f:
            noun = random.choice(f.read().splitlines())
        f.close()

        with open(WORDS_DIR + '/adjectives.txt') as f:
            adj = random.choice(f.read().splitlines())
            f.close()

        with open(WORDS_DIR + '/verbs.txt') as f:
            verb = random.choice(f.read().splitlines())
        f.close()

        choices = ['{} of {}'.format(noun.upper(), name), '{} {}'.format(noun.upper(), noun), '{} {}'.format(verb.upper(), noun), '{} {}'.format(adj.upper(), noun) ]

        return(random.choice(choices))


class InGame(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    class Meta:
        unique_together = ('game', 'player')
