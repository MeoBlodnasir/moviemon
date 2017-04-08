import requests
import json
from django.conf import settings
import random

class Data():
    movies = []
    player_strength = 0
    def load_default_settings(self):
        for elem in settings.MOVIES:
            r = requests.get("http://www.omdbapi.com/?t=" + elem.replace(" ", "+"))
            print(elem, r)
            d = json.loads(r.text)
            if 'Title' in d:
                self.movies.append({'title': d['Title'], 'rating' : d['imdbRating']})
        return self

    def load(self, dic):
        for key, value in dic:
            if key == 'movies':
                self.movies = value
            elif key == 'player_strength':
                self.player_strength = value
    def dump(self, dic):
        return {'movies': self.movies, 'player_strength' : self.player_strength}
    def get_random_movie(self):
        return random.choice(list(self.movies))
    def get_movie(self, title):
        for elem in self.movies:
            if elem['title'] == title:
                return elem


