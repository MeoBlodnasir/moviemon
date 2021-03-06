from django.shortcuts import render, HttpResponse
from . import forms
from .tool.game.Page import Page
from .tool.game import elements as e
from .tool.game.elem import Text
from .tool.game.worldmap import worldmap, worldmap_render
from .tool.game.options import Options, options_render, save_render, load_render
from .tool.game.titlescreen import Titlescreen, titlescreen_render
from .tool.game.fight import fight, fight_render
from .tool.game.moviedex import Moviedex, moviedex_render, movie_render
# Create your views here.

def titlescreen(request):
    return (titlescreen_render(request))

def worldmap(request):
    return (worldmap_render(request))

def fight(request, movimone=''):
    return (fight_render(request, movimone))

def options(request):
    return (options_render(request))

def save(request):
    return (save_render(request))

def load(request):
    return (load_render(request))

def moviedex(request):
    return (moviedex_render(request))

def movie(request, moviemon=''):
    return (movie_render(request, moviemon))
