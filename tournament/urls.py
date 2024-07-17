# tournament/urls.py

from django.urls import path
from .views import PlayerViewSet, TournamentViewSet, MatchViewSet

player_list = PlayerViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

player_detail = PlayerViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

tournament_list = TournamentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

tournament_detail = TournamentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

match_list = MatchViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

match_detail = MatchViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('players/', player_list, name='player-list'),
    path('players/<int:pk>/', player_detail, name='player-detail'),
    path('tournaments/', tournament_list, name='tournament-list'),
    path('tournaments/<int:pk>/', tournament_detail, name='tournament-detail'),
    path('matches/', match_list, name='match-list'),
    path('matches/<int:pk>/', match_detail, name='match-detail'),
]
