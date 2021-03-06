from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from . import elements as e
from .data import Data
from .elem import Text
import os
from django.conf import settings

class Options(Data):
    def __init__(self):
        content = [Text('A - Save<br/>B - Quit</br>Start - Cancel</br>')]
        style = 'height:' + str(settings.MAP['h']) + 'px; width:' +  str(settings.MAP['w']) + 'px;'
        self.options = e.Div(content, attr={'class':'container', 'style': style})
    def __str__(self):
        return str(self.options)

options = Options()

def options_render(request):
    if (request.method == 'POST'):
        if 'Start' in request.POST:
            return HttpResponseRedirect('/worldmap')
        elif 'A' in request.POST:
            return HttpResponseRedirect('/options/save_game')
        elif 'B' in request.POST:
            if (os.path.isfile("saved_game/tmp_save")):
                os.remove("saved_game/tmp_save")
            return HttpResponseRedirect('/')

    return render(request, "game/options.html", {'options': options})


class Save(Data):
    marker = 0
    def __init__(self):
        i = 0;
        content = []
        for elem in self.saves:
            if i == Save.marker:
                content.append(Text('==> '))
            content.append(Text("Slot {0} : ".format(elem['name']).upper()))
            if elem['free'] == True:
                content.append(Text(" FREE<br/>"))
            else:
                content.append(Text("   score: " + str(elem['score']) + "<br/>"))
            i += 1
        content.append(Text('A - Save<br/>B - Cancel</br>'))
        style = 'height:' + str(settings.MAP['h']) + 'px; width:' +  str(settings.MAP['w']) + 'px;'
        self.text = e.Div(content, attr={'class':'container', 'style': style})
    def __str__(self):
        return str(self.text)


def save_render(request):
    if (request.method == 'POST'):
        if 'Down' in request.POST and Save.marker < 2:
                Save.marker += 1
                return render(request, "game/save.html", {'save': Save()})
        if 'Up' in request.POST and Save.marker > 0:
                Save.marker -= 1
                return render(request, "game/save.html", {'save': Save()})
        if 'A' in request.POST:
            s = Save()
            s.save_slot(s.saves[Save.marker]['name'])
            return render(request, "game/save.html", {'save': Save()})
        if 'B' in request.POST:
            return HttpResponseRedirect('/options')

    return render(request, "game/save.html", {'save': Save()})

class Load(Data):
    marker = 0
    loaded = False
    def __init__(self):
        i = 0;
        content = []
        for elem in self.saves:
            if i == Load.marker:
                content.append(Text('==> '))
            content.append(Text("Slot {0} : ".format(elem['name']).upper()))
            if elem['free'] == True:
                content.append(Text(" FREE<br/>"))
            else:
                content.append(Text("   score: " + str(elem['score']) + "<br/>"))
            i += 1
        if Load.loaded == False:
            content.append(Text('A - Load<br/>B - Cancel</br>'))
        else:
            content.append(Text('A - start game<br/>B - Cancel</br>'))
        style = 'height:' + str(settings.MAP['h']) + 'px; width:' +  str(settings.MAP['w']) + 'px;'
        self.text = e.Div(content, attr={'class':'container', 'style':style})
    def __str__(self):
        return str(self.text)

def load_render(request):
    if (request.method == 'POST'):
        if 'Down' in request.POST and Load.marker < 2:
                Load.marker += 1
                return render(request, "game/load.html", {'load': Load()})
        if 'Up' in request.POST and Load.marker > 0:
                Load.marker -= 1
                return render(request, "game/load.html", {'load': Load()})
        if Load.loaded == True:
            if 'A' in request.POST:
                Load.loaded = False
                return HttpResponseRedirect('/worldmap')
        if 'A' in request.POST:
            s = Load()
            if s.load_slot(s.saves[Load.marker]['name']) == 1:
                Load.loaded = True
            else :
                return render(request, "game/load.html", {'load': Load()})
        if 'B' in request.POST:
            return HttpResponseRedirect('/options')

    return render(request, "game/load.html", {'load': Load()})
