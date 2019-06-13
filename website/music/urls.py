from django.conf.urls import url
from . import views

# . means current file
app_name="music"
urlpatterns = [
    #/music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    #/music/123 or album id/(lecture 12 tnb for this r.e.) #for url pattern
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),

    '''#/music/123 or album id/favorite /(lecture 22)
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name="favorite "),'''
]