from django.shortcuts import render, HttpResponse
import random

from .Page import Page
from . import elements as e
from .elem import Text
from .data import Data



class worldmap(Data):
    movieballs = 0
    """docstring for worldmap."""
    def __init__(self, setting, user):
        print("init --------------------------")
        self.load_default_settings()
        self.setting = setting
        self.user = user
        self.is_movies_found = False
        self.create_map(setting, user, False)

    def __str__(self):
        return str(self.map)

    def random_meet(self, is_moving):
        attr = {}
        self.is_movies_found = False
        if is_moving:
            is_movieball = False
            if random.randrange(0, 3) == 0:
                is_movieball = True
                self.movieballs += 1
                self.player_strength += 1
                attr = {'src':'http://belleetcultivee.com/wp-content/uploads/2012/02/cd.gif'}
            if is_movieball == False:
                if random.randrange(0, 3) == 0:
                    movie = self.get_random_movie()
                    self.is_movies_found = True
                    self.movie = self.get_random_movie()
                    attr = {'src':'http://www.citel.fr/userfiles/medias/photo/Foudre_bleu.gif'}
        return attr

    def create_map(self, setting=None, user=None, is_moving=False):
        if setting == None:
            self.setting = self.setting
        else:
            self.setting = setting
        self.user = user
        self.random_meet(True)
        top = self.user['pos_y'] * self.setting['h'] / self.setting['y'] - self.setting['h'] / self.setting['y'] / 2
        left = self.user['pos_x'] * self.setting['h'] / self.setting['x'] - self.setting['w'] / self.setting['x'] / 2
        if top < 0:
            top *= -1
        if left < 0:
            left *= -1
        style = 'top:' + str(int(top)) + 'px;' + ' left:' + str(int(left)) + 'px; position: absolute'
        player = e.Div(Text('X'), attr={'class':'player', 'style':style})
        content = []
        content.append(player)

        if self.is_movies_found:
            content.append(e.Div(Text('Enter a for the fight with ' + str(self.movie['title']))))
        self.map = e.Div(content, attr={'class': 'container', 'style':'height: 1000px; width: 1000px; position:relative'})

setting = {'x': 10, 'y' : 10, 'h' : 1000, 'w' : 1000}
user = {'pos_x': 0, 'pos_y':0}

map = worldmap(setting, user)


def worldmap_render(request):

    is_moving = False

    if (request.method == 'POST'):
        if 'A' in request.POST:
            pass
        if 'Up' in request.POST:
            if (user['pos_y'] - 1) >= 0:
                user['pos_y'] -= 1
                is_moving = True
        if 'Down' in request.POST:
            if (user['pos_y'] + 1) < setting['y']:
                user['pos_y'] += 1
                is_moving = True
        if 'Right' in request.POST:
            if (user['pos_x'] + 1) < setting['x']:
                user['pos_x'] += 1
                is_moving = True
        if 'Left' in request.POST:
            if (user['pos_x'] - 1) >= 0:
                user['pos_x'] -= 1
                is_moving = True
    if is_moving:
        map.create_map(setting, user, is_moving)
    movieballs_nb = e.Div(Text(str(map.player_strength)))
    return render(request, "game/worldmap.html", {'map':map, 'movieballs_nb':movieballs_nb})
