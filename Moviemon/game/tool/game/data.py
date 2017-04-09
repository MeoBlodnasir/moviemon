import requests
import json
from django.conf import settings
import random
import pickle
import glob
import os

class Data():

    movies = []
    player_strength = 0
    score = 0
    moviemon = ''
    player = {}
    saves = []
    is_movies_found = False
    movie = {}
    moviemon_captured = []
    is_captured = False
    if not glob.glob('saved_game/slota*'):
        saves.append({'name': 'a', 'free': True, 'score' : 0})
    if not glob.glob('saved_game/slotb*'):
        saves.append({'name': 'b', 'free': True, 'score' : 0})
    if not glob.glob('saved_game/slotc*'):
        saves.append({'name': 'c', 'free': True, 'score' : 0})

    for i in os.listdir('saved_game'):
        if os.path.isfile(os.path.join('saved_game',i)) and 'slot' in i:
            if i[7:8] == '_':
                saves.append({'name': i[4:5], 'free': False, 'score': int(i[6:7])})
            else:
                saves.append({'name': i[4:5], 'free': False, 'score': int(i[6:8])})


    def load_default_settings(self):
        self.setting = {'x': 10, 'y' : 10, 'h' : 1000, 'w' : 1000}
        if len(self.movies) == 0:
            for elem in settings.MOVIES:
                r = requests.get("http://www.omdbapi.com/?t=" + elem.replace(" ", "+"))
                print(elem, r)
                d = json.loads(r.text)
                if 'Title' in d:
                    self.movies.append({'title': d['Title'], 'rating' : d['imdbRating'], 'year' : d['Year'], 'director': d['Director'], 'poster' : d['Poster'], 'plot' : d['Plot'], 'actors' : d['Actors']})
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
            elif key == 'is_movies_found':
                self.is_movies_found = value
            elif key == 'movie':
                self.movie = value
            elif key == 'is_captured':
                self.is_captured = value
            elif key == 'moviemon_captured':
                self.moviemon_captured = value

    def dump(self):
        return {'movies': self.movies, 'player_strength' : self.player_strength, 'score': self.score, 'saves': self.saves, 'player': self.player, 'is_movies_found': self.is_movies_found, 'movie':self.movie, 'is_captured': self.is_captured,'moviemon_captured' : self.moviemon_captured}
    def get_random_movie(self):
        movie = random.choice(list(self.movies))
        for v in self.moviemon_captured:
            if v['title'] == movie['title']:
                return self.get_random_movie()
        return movie
    def get_captured_movies(self):
        return self.moviemon_captured
    def get_movie(self, title):
        for elem in self.movies:
            if elem['title'] == title:
                return elem
        return {'title': 'unknown'}
    def save_slot(self, slot):
        try:
            if slot == 'a' or slot == 'b' or slot == 'c':
                pickle.dump(pickle.load(open("saved_game/tmp_save", "rb")), open("saved_game/slot{0}_{1}_15.mmg".format(slot, self.score), "wb+" ))
                for elem in self.saves:
                    if elem['name'] == slot:
                        elem['free'] = False
                        elem['score'] = self.score
        except Exception as e:
            print(e)

    def load_slot(self, slot):
        try:
            if (slot == 'a' or slot == 'b' or slot == 'c'):
                for elem in self.saves:
                    if elem['name'] == slot and elem['free'] == False:
                        pickle.dump(pickle.load(open("saved_game/slot{0}_{1}_15.mmg".format(slot, self.score), "rb")),open("saved_game/tmp_save", "wb"))
                        self.load(pickle.load(open("saved_game/tmp_save", "rb")))
                        return 1
            return -1
        except Exception as e:
            print(e)

    def load_tmp(self):
        try:
            if os.path.isfile('saved_game/tmp_save'):
                self.load(pickle.load(open("saved_game/tmp_save", "rb")))
            else:
                self.load({'player': {'pos_x': 1, 'pos_y': 1}, 'score': 0, 'player_strength': 0, 'is_movies_found': False, 'moviemon_captured': []})
                self.save_tmp()
        except Exception as e:
            print(e)

    def save_tmp(self):
        try:
            pickle.dump(self.dump(), open("saved_game/tmp_save", "wb+" ))
        except Exception as e:
            print(e)
