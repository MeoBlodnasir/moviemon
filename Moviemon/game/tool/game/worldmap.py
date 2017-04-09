from django.shortcuts import render, HttpResponse, HttpResponseRedirect
import random

from .Page import Page
from . import elements as e
from .elem import Text
from .data import Data



class worldmap(Data):
    movieballs = 0
    is_movies_found = False
    """docstring for worldmap."""
    def __init__(self):
        self.load_default_settings()
        self.load_tmp()
        # worldmap.is_movies_found = False
        self.create_map(False)

    def __str__(self):
        return str(self.map)

    def random_meet(self, is_moving):
        attr = {}
        worldmap.is_movies_found = False
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
                    worldmap.is_movies_found = True
                    self.movie = self.get_random_movie()
                    attr = {'src':'http://www.citel.fr/playerfiles/medias/photo/Foudre_bleu.gif'}
        return attr

    def create_map(self, is_moving=False):
        self.random_meet(True)
        top = self.player['pos_y'] * self.setting['h'] / self.setting['y'] - self.setting['h'] / self.setting['y'] / 2
        left = self.player['pos_x'] * self.setting['h'] / self.setting['x'] - self.setting['w'] / self.setting['x'] / 2
        if top < 0:
            top *= -1
        if left < 0:
            left *= -1
        style = 'top:' + str(int(top)) + 'px;' + ' left:' + str(int(left)) + 'px; position: absolute'
        player = e.Div(Text('X'), attr={'class':'player', 'style':style})
        content = []
        content.append(player)

        if worldmap.is_movies_found:
            content.append(e.Div(Text('Enter a for the fight with ' + str(self.movie['title']))))
        content.append(e.Div(Text(str(self.player_strength))))
        self.map = e.Div(content, attr={'class': 'container'})

        self.save_tmp()

setting = {'x': 10, 'y' : 10, 'h' : 1000, 'w' : 1000}
player = {'pos_x': 0, 'pos_y':0}




def worldmap_render(request):
    map = worldmap()
    is_moving = False

    if (request.method == 'POST'):
        if 'A' in request.POST :
            if worldmap.is_movies_found:
                return(HttpResponseRedirect('/battle/' + str(map.movie['title']).replace(' ', '_')))
        if 'Up' in request.POST:
            if (map.player['pos_y'] - 1) >= 0:
                map.player['pos_y'] -= 1
                is_moving = True
        if 'Down' in request.POST:
            if (map.player['pos_y'] + 1) < setting['y']:
                map.player['pos_y'] += 1
                is_moving = True
        if 'Right' in request.POST:
            if (map.player['pos_x'] + 1) < setting['x']:
                map.player['pos_x'] += 1
                is_moving = True
        if 'Left' in request.POST:
            if (map.player['pos_x'] - 1) >= 0:
                map.player['pos_x'] -= 1
                is_moving = True
        if 'Start' in request.POST:
            return HttpResponseRedirect('/options')
    if is_moving:
        map.create_map(is_moving)
    # movieballs_nb =
    return render(request, "game/worldmap.html", {'map':map})
