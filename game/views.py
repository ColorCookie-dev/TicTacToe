from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.views import generic
from gameserver.GameControl import CreateGame, RetGame


def game(request, tiles):

    # Checking if no. of tiles is very high or low
    if tiles > 20 or tiles < 3:
        return HttpResponseBadRequest("<h1>No of tiles is not in bound [3,20]!")

    return render(request, 'game/game.html', {
        'tiles': tiles,
        'tiles_range': range(tiles),
        })

def create_game(request, tiles=3):
    game_id = CreateGame(tiles)
    return HttpResponseRedirect("/?gid={}".format(game_id))
