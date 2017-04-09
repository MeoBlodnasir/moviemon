from django.shortcuts import render, HttpResponse
from . import forms
from .tool.game.Page import Page
from .tool.game import elements as e
from .tool.game.elem import Text
from .tool.game.worldmap import worldmap, worldmap_render
from .tool.game.fight import fight, fight_render
# Create your views here.

def titlescreen(request):
    if (request.method == 'POST'):
        print(request.POST)
        if 'A' in request.POST:
            return render(request, "game/worldmap.html")
        elif 'B' in request.POST:
            return HttpResponse("other key")
        else:
            return render(request, "game/controls.html")


    else:
        return render(request, "game/controls.html")

def worldmap(request):
    return (worldmap_render(request))

def fight(request, movimone=''):
    return (fight_render(request, movimone))

def options(request):
    return (options_render(request))
