from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic


def SingleGameView(request):
    return render(request, 'game/game.html', {
            'single': True,
            'row_range': range(3),
            'col_range': range(3),
        })

def MultiGameView(request):
    return render(request, 'game/game.html', {
            'single': False,
            'row_range': range(3),
            'col_range': range(3),
        })

def game(request, game_id):
    pass
