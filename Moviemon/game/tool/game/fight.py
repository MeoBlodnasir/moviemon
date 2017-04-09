from django.shortcuts import render, HttpResponse, HttpResponseRedirect
import random

from .Page import Page
from . import elements as e
from .elem import Text
from .data import Data

class fight(Data):
    def __init__(self, moviemon=''):
        print('---------init------------')
        self.load_tmp()
        self.moviemon = self.get_movie(moviemon)
        self.is_captured = False
        self.launch = False
        self.mess = ''

    def __str__(self):
        content = []
        content.append(e.Div(e.Text(str(self.moviemon['title']) + ' force: ' + str(self.moviemon['rating']) )))
        content.append(e.Div(e.Text('A - Launch movieball')))
        content.append(e.Div(Text('Player force: ' + str(battle.player_strength))))
        if self.launch:

        return str(e.Div(content, attr={'class':'container'}))

    def set_moviemon(self, moviemon):
        self.mess = ''
        self.is_captured = False
        self.launch = False
        self.load_tmp()
        self.moviemon = self.get_movie(moviemon)

    def chance_to_catch(self):
        c = 50 - (self.moviemon['rating'] * 10) + (self.player_strength * 5)
        if c < 1:
            c = 1
        if c > 99:
            c = 90
        return int(c)

    def launch_movieball(self):
        if self.player_strength == 0:
            return
        self.launch = True
        c = self.chance_to_catch()
        r = random(0, 100)
        if r <= c:
            self.is_captured = True
            self.movie.append(self.moviemon)
        self.player_strength -= 1
        self.save_tmp()

battle = fight()

def fight_render(request, moviemon):
    moviemon = moviemon.replace('_', ' ')
    if battle.moviemon != moviemon:
        battle.set_moviemon(moviemon)
    if 'B' in request.POST :
        return(HttpResponseRedirect('/worldmap'))

    return render(request, "game/worldmap.html", {'map':battle})
