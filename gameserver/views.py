# from django.shortcuts import render
from django.http import JsonResponse, Http404
from . import GameControl

def GameServer(request, tiles):
    
    if request.method == 'POST':
        if 'gid' not in request.POST.keys():
            # Game Creation
            if 'init' not in request.POST.keys():
                raise Http404("Bad Request!")
            return JsonResponse(GameControl.CreateGame(tiles))
        else:
            # Getting Game State
            gameobj = GameControl.RetGame(request.POST['gid'])
            if not gameobj:
                raise Http404("Bad Request")
            if 'move[]' in request.POST.keys():
                if not GameControl.Move(request.POST['gid'], request.POST.getlist('move[]')):
                    raise Http404("Bad Request")
            return JsonResponse(gameobj)
    else:
        raise Http404("Bad Request!")
