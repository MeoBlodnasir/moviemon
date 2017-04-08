import requests
import json
from django.conf import settings
import random
import pickle

class Data():
    movies = []
    player_strength = 0
    score = 0
    saves = [{'name': 'a', 'free': True, 'score' : 0},{'name': 'b', 'free': True, 'score' : 0},{'name': 'c', 'free': True, 'score' : 0}]
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
            elif key == 'score':
                self.score = value
            elif key == 'saves':
                self.saves = value
    def dump(self):
        return {'movies': self.movies, 'player_strength' : self.player_strength, 'score': self.score, 'saves': self.saves}
    def get_random_movie(self):
        return random.choice(list(self.movies))
    def get_movie(self, title):
        for elem in self.movies:
            if elem['title'] == title:
                return elem
    def save(self, slot):
        if slot == 'a' or slot == 'b' or slot == 'c':
            pickle.dump(pickle.load(open("saved_game/tmp_save", "rb")), open("saved_game/slot{0}_{1}_15.mmg".format(slot, self.score), "wb+" ))
            for elem in saves:
                if elem['name'] == slot:
                    elem['free'] = M#False

    def load(self, slot):
        if (slot == 'a' or slot == 'b' or slot == 'c'):
            for elem in saves:
                if elem['name'] == slot and elem['free'] == False:
                    pickle.dump(pickle.load(open("saved_game/slot{0}_{1}_15.mmg".format(slot, self.score), "rb")),open("saved_game/tmp_save", "rb"))
                    self.load(pickle.load(open("saved_game/tmp_save", "rb")))
