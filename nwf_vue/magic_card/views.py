from django.shortcuts import render

# Create your views here.
api_view(['GET', 'POST'])
def submit_card(request):
    #Retrieve game object
    game = Game.objects.get(pk=game)
    if request.method == 'POST':
        #Create the magic card object
        card = MagicCard.objects.create(
                player = User.objects.get(username=request.username),
                game = game,
                round_submitted = request.round_submitted,
                card_name = request.card_name,
                submitted = True,
                card_color = request.card_color,
                card_type = request.card_type,
                converted_mana_cost = request.converted_mana_cost,
                card_text = request.card_text,
                flavor_text = request.flavor_text

        )
    game.submissions +=1

    data = MagicCardSerializer(card)
    return Response(data)
