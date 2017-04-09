from django.shortcuts import render, HttpResponse
import random

from .Page import Page
from . import elements as e
from .elem import Text
from .data import Data

class fight(Data):
    def __init__(self, moviemon=''):
        print('---------init------------')
        self.load_tmp()
        self.moviemon = moviemon
        # self.error = False
        # self.movieballs = Data.player_strength
        # if self.moviemon != self.__class__.moviemon:
        #     print('Error')
        #     pass
    def __str__(self):
        content = []
        content.append(e.Div(e.Text(str(self.moviemon))))
        return str(e.Div(content, attr={'class':'container'}))

    def set_moviemon(self, moviemon):
        self.load_tmp()
        self.moviemon = moviemon

    def fname(arg):
        pass
battle = fight()

def fight_render(request, moviemon):
    if battle.moviemon != moviemon:
        battle.set_moviemon(moviemon)
    movieballs_nb = e.Div(Text(str(battle.player_strength)))
    print('player_strength', battle.player_strength)
    return render(request, "game/worldmap.html", {'map':battle, 'movieballs_nb':movieballs_nb})
