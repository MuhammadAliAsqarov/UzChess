# tournament/admin.py

from django.contrib import admin
from .models import Player, Tournament, Match

admin.site.register(Player)
admin.site.register(Tournament)
admin.site.register(Match)
