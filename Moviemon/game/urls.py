from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.titlescreen),
        url(r'^worldmap$', views.worldmap),
        url(r'^battle/(?P<moviemon_id>\d+)/$', views.fight),
        url(r'^options$', views.options),
        url(r'^options/save_game$', views.save),
        url(r'^options/load_game$', views.load),
        ]
