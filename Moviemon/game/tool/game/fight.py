from django.shortcuts import render, HttpResponse, HttpResponseRedirect
import random

from .Page import Page
from . import elements as e
from .elem import Text
from .data import Data

class fight(Data):
    launch = False
    def __init__(self, moviemon=''):
        print('---------init------------')
        self.load_default_settings()
        self.load_tmp()
        self.moviemon = self.get_movie(moviemon)
        self.is_captured = False
        self.mess = ''

    def __str__(self):
        content = []
        content.append(e.Div(e.Text(str(self.moviemon['title']) + ' force: ' + str(self.moviemon['rating']) )))
        content.append(e.Div(e.Text('A - Launch movieball')))
        content.append(e.Div(Text('Player force: ' + str(self.player_strength))))
        if fight.launch:
            content.append(e.Div(e.Text(self.mess)))
        return str(e.Div(content, attr={'class':'container'}))

    def set_moviemon(self, moviemon):
        self.mess = ''
        self.is_captured = False
        # self.launch = False
        # self.load_tmp()
        self.moviemon = self.get_movie(moviemon)
        # for v in self.movies:
        #     if v['title'] == self.moviemon['title']:
        #         self.is_captured = True

    def chance_to_catch(self):
        c = 50 - (float(self.moviemon['rating']) * 10) + (float(self.player_strength) * 5)
        if c < 1:
            c = 1
        if c > 99:
            c = 90
        return int(c)

    def is_captured_list(self, target):
        print('list', self.moviemon_captured)
        for v in self.moviemon_captured:
            if v['title'] == target['title']:
                return True
        return False

    def launch_movieball(self):
        print('ll', self.player_strength, self.is_captured)
        if self.player_strength == 0:
            self.mess = "No more movieballs !"
            return
        if self.is_captured_list(self.moviemon):
            self.mess = "You catched it"
            return
        print('  ll  pp ')
        fight.launch = True
        c = self.chance_to_catch()
        r = random.randrange(0, 100)
        if r <= c:
            self.is_captured = True
            self.score += 1
            self.moviemon_captured.append(self.moviemon)
            self.mess = "You catched it"
        else:
            self.mess = "You missed !"
        self.is_movies_found = False
        self.player_strength -= 1
        self.save_tmp()

def fight_render(request, moviemon):
    moviemon = moviemon.replace('_', ' ')
    battle = fight()
    battle.set_moviemon(moviemon)
    if 'B' in request.POST :
        return(HttpResponseRedirect('/worldmap'))
    if 'A' in request.POST :
        print('f A')
        battle.launch_movieball()

    return render(request, "game/worldmap.html", {'map':battle})
