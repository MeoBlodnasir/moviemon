from django.shortcuts import render, HttpResponse, HttpResponseRedirect
import random
from django.conf import settings
from .Page import Page
from . import elements as e
from .elem import Text
from .data import Data



class worldmap(Data):
    movieballs = 0
    """docstring for worldmap."""
    def __init__(self):
        self.load_default_settings()
        self.load_tmp()
        self.create_map(False)
        self.is_message = False

    def __str__(self):
        return str(self.map)

    def random_meet(self, is_moving):
        attr = {}
        self.is_message = False
        if is_moving:
            self.is_movies_found = False
            is_movieball = False
            if random.randrange(0, 3) == 0:
                is_movieball = True
                self.movieballs += 1
                self.player_strength += 1
                self.is_message = True
                attr = {'src':'http://belleetcultivee.com/wp-content/uploads/2012/02/cd.gif'}
            if is_movieball == False:
                if random.randrange(0, 3) == 0:
                    movie = self.get_random_movie()
                    self.is_movies_found = True
                    self.movie = self.get_random_movie()
                    attr = {'src':'http://www.citel.fr/playerfiles/medias/photo/Foudre_bleu.gif'}
        return attr

    def create_map(self, is_moving=False):
        self.random_meet(is_moving)
        top = self.player['pos_y'] * settings.MAP['h'] / settings.MAP['y'] - settings.MAP['h'] / settings.MAP['y'] / 2
        left = self.player['pos_x'] * settings.MAP['h'] / settings.MAP['x'] - settings.MAP['w'] / settings.MAP['x'] / 2
        if top < 0:
            top *= -1
        if left < 0:
            left *= -1
        style = 'top:' + str(int(top)) + 'px;' + ' left:' + str(int(left)) + 'px; position: absolute'
        player = e.Div(Text('X'), attr={'class':'player', 'style':style})
        content = []
        content.append(player)


        content.append(e.Div(Text(str(self.player_strength))))
        if self.is_movies_found:
            content.append(e.Div(Text('Enter a for the fight with ' + str(self.movie['title']))))
        if self.is_message:
            content.append(e.Div(Text('Movieball found')))
        style = 'height:' + str(settings.MAP['h']) + 'px; width:' +  str(settings.MAP['w']) + 'px;'

        self.map = e.Div(content, attr={'class': 'container', 'style': style})

        self.save_tmp()

def worldmap_render(request):
    map = worldmap()
    is_moving = False

    if (request.method == 'POST'):
        if 'A' in request.POST :
            print('-A')
            if map.is_movies_found:
                print('found')
                return(HttpResponseRedirect('/battle/' + str(map.movie['title']).replace(' ', '_')))
        if 'Up' in request.POST:
            if (map.player['pos_y'] - 1) >= 1:
                map.player['pos_y'] -= 1
                is_moving = True
        if 'Down' in request.POST:
            if (map.player['pos_y'] + 1) <= settings.MAP['y']:
                map.player['pos_y'] += 1
                is_moving = True
        if 'Right' in request.POST:
            if (map.player['pos_x'] + 1) <= settings.MAP['x']:
                map.player['pos_x'] += 1
                is_moving = True
        if 'Left' in request.POST:
            if (map.player['pos_x'] - 1) >= 1:
                map.player['pos_x'] -= 1
                is_moving = True
        if 'Start' in request.POST:
            return HttpResponseRedirect('/options')
        if 'Select' in request.POST:
            return HttpResponseRedirect('/moviedex')
    if is_moving:
        map.create_map(is_moving)
    return render(request, "game/worldmap.html", {'map':map})
