from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from . import elements as e
from .data import Data
from .elem import Text
import os.path


class Titlescreen():
    def __init__(self):
        content = []
        content.append(Text("A - New Game<br/>B - Load<br/>"))
        self.titlescreen = e.Div(content, attr={'class':'containter'})
    def __str__(self):
        return str(self.titlescreen)

def titlescreen_render(request):
    if (request.method == 'POST'):
        if 'A' in request.POST:
            if (os.path.isfile("saved_game/tmp_save")):
                os.remove("saved_game/tmp_save")
            return HttpResponseRedirect('/worldmap')
        if 'B' in request.POST:
            return HttpResponseRedirect('/options/load_game')

    return render(request, "game/titlescreen.html", {'titlescreen': Titlescreen()})
