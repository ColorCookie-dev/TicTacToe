from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic


def game(request):
    divide = 5
    return render(request, 'game/game.html', {
            'divide': divide,
            'divide_range': range(divide),
        })

# def game(request, game_id):
    # pass
