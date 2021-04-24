from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.


@login_required
def tour(request):
    # Display all actions by default
    tours = kfupm_tournament.objects.all()



    return render(request,
                  'tour/tour.html',
                  {'section': 'tour',
                    'tours':tours})


@login_required
def teams(request, id):
    # Display all actions by default
    tour = get_object_or_404(kfupm_tournament,
                             id=id)

    teams = tour.teams.all()
    best_players_dic = {}
    best_players = []
    players_not_having_cards = []
    players_not_having_cards_dic = {}

    i = 0
    for team in teams:
        players_not_having_cards_dic[team] = []
        best_player = None
        players = team.players.all()
        players_not_having_cards.append([])
        for player in players:
            if best_player == None:
                best_player = player
            else:
                if player.goals.count() > best_player.goals.count():
                    best_player = player
            if player.cards.count()==0:
                players_not_having_cards_dic[team].append(player)
                players_not_having_cards[i].append(player)
        i+=1
        if best_player != None and best_player.goals.count() >0:
            #team = best_player.teams
            best_players_dic[team] = best_player
            best_players.append(best_player)
    
    #print(players_not_having_cards)
    #print(best_players)


    return render(request,
                  'tour/teams.html',
                  {'section': 'tour','teams':teams,
                    'best_players': best_players,'no_cards':players_not_having_cards,'best_players_dic':best_players_dic,'no_cards_dic':players_not_having_cards_dic})