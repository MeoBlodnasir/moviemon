from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.titlescreen),
        url(r'^worldmap$', views.worldmap),
        url(r'^options$', views.options),
        url(r'^options/save_game$', views.save),
        url(r'^options/load_game$', views.load),
        url(r'^battle/(?P<movimone>\w+)$', views.fight),
        url(r'^moviedex/(?P<moviemon>\w+)$', views.movie),
        url(r'^moviedex$', views.moviedex),
        ]
