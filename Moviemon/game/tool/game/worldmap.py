from django.shortcuts import render, HttpResponse
import random

from .Page import Page
from . import elements as e
from .elem import Text

class worldmap:
    movieballs = 0
    """docstring for worldmap."""
    def __init__(self, setting, user):
        pass
        self.setting = setting
        self.user = user
        # self.create_map(setting, user)

    def random_meet(self, is_moving):
        attr = {}
        if is_moving:
            is_movieball = False
            if random.randrange(0, 3) == 0:
                is_movieball = True
                self.movieballs += 1
                attr = {'src':'http://belleetcultivee.com/wp-content/uploads/2012/02/cd.gif'}
            if is_movieball == False:
                if random.randrange(0, 3) == 0:
                    attr = {'src':'http://www.citel.fr/userfiles/medias/photo/Foudre_bleu.gif'}
        return attr
    def create_map(self, setting=None, user=None, is_moving=False):
        if setting == None:
            self.setting = self.setting
        else:
            self.setting = setting
        self.user = user
        table = []
        y = 0
        while y < self.setting['y']:
            tr = []
            x = 0
            while x < self.setting['x']:
                if x == self.user['pos_x'] and y == self.user['pos_y']:
                    attr = self.random_meet(is_moving)
                    td = e.Td(e.Div([e.Img(attr=attr ), Text('Yo') ]))
                else:
                    td = e.Td(e.Div(attr={'class': 'cell'}))
                tr.append(td)
                x += 1
            y += 1

            table.append(e.Tr(tr))
        self.map = e.Table(table)

setting = {'x': 10, 'y' : 10}
user = {'pos_x': 0, 'pos_y':0}

map = worldmap(setting, user)

def worldmap_render(request):
    is_moving = False
    if (request.method == 'POST'):
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
    map.create_map(setting, user, is_moving)
    page = Page(e.Div(map.map))
    return render(request, "game/worldmap.html", {'map':map.map})
