from django.shortcuts import render, HttpResponse
from . import forms

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

