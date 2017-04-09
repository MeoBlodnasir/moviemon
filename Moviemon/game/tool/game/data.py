import requests
import json
from django.conf import settings
import random
import pickle
import os

class Data():

    movies = []
    player_strength = 0
    score = 0
    moviemon = ''
    player = {}
    saves = [{'name': 'a', 'free': True, 'score' : 0},{'name': 'b', 'free': True, 'score' : 0},{'name': 'c', 'free': True, 'score' : 0}]

    def load_default_settings(self):
        self.setting = {'x': 10, 'y' : 10, 'h' : 1000, 'w' : 1000}
        for elem in settings.MOVIES:
            r = requests.get("http://www.omdbapi.com/?t=" + elem.replace(" ", "+"))
            print(elem, r)
            d = json.loads(r.text)
            if 'Title' in d:
                self.movies.append({'title': d['Title'], 'rating' : d['imdbRating'], 'year' : d['Year'], 'director': d['Director']})
        return self

    def load(self, dic):
        for key, value in dic.items():
            if key == 'movies':
                self.movies = value
            elif key == 'player_strength':
                self.player_strength = value
            elif key == 'score':
                self.score = value
            elif key == 'saves':
                self.saves = value
            elif key == 'player':
                self.player = value
    def dump(self):
        return {'movies': self.movies, 'player_strength' : self.player_strength, 'score': self.score, 'saves': self.saves, 'player': self.player}
    def get_random_movie(self):
        return random.choice(list(self.movies))
    def get_movie(self, title):
        for elem in self.movies:
            if elem['title'] == title:
                return elem
    def save_slot(self, slot):
        if slot == 'a' or slot == 'b' or slot == 'c':
            pickle.dump(pickle.load(open("saved_game/tmp_save", "rb")), open("saved_game/slot{0}_{1}_15.mmg".format(slot, self.score), "wb+" ))
            for elem in self.saves:
                if elem['name'] == slot:
                    elem['free'] = False

    def load_slot(self, slot):
        if (slot == 'a' or slot == 'b' or slot == 'c'):
            for elem in self.saves:
                if elem['name'] == slot and elem['free'] == False:
                    pickle.dump(pickle.load(open("saved_game/slot{0}_{1}_15.mmg".format(slot, self.score), "rb")),open("saved_game/tmp_save", "rb"))
                    self.load(pickle.load(open("saved_game/tmp_save", "rb")))

    def load_tmp(self):
        if os.path.isfile('saved_game/tmp_save'):
            self.load(pickle.load(open("saved_game/tmp_save", "rb")))
        else:
            self.load({'player': {'pos_x': 0, 'pos_y': 0}, 'score': 0, 'player_strength': 0})
            self.save_tmp()

    def save_tmp(self):
        # print(self.dump())
        print('save_tmp', self.player_strength)
        pickle.dump(self.dump(), open("saved_game/tmp_save", "wb+" ))
