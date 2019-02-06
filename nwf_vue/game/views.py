from django.shortcuts import render
from magic_card.models import MagicCard
from game.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


#################################
api_view(['GET', 'POST'])
def create_game(request):

    if request.method == 'POST':
        game = Game.objects.create(
            number_of_players = request.number_of_players,
            number_of_rounds = request.number_of_rounds,
            card_name = Game.get_card_name(),
            name = Game.game_name(),
        )
        data = GameSerializer(game)
        return Response(data)

#####################################
api_view(['GET', 'POST'])
def join_game(request):
    #Retrieve game object
    game = Game.objects.get(pk=request.game)
    if request.method == 'POST':
        #Create an InGame object for player
        InGame.objects.create(
            player = User.objects.get(username=request.player),
            game = game
            )

    if length(game.players) == game.number_of_players:

        subject = 'Game is ready to begin'
        message = 'Your game has enough players to begin, please follow the link to submit a card'
        game.notify_players(subject=subject,message=message)

    #return updated game object
    data = GameSerializer(game)
    return Response(data)

###################################

api_view(['GET', 'POST'])
def end_game(request):
    pass 
