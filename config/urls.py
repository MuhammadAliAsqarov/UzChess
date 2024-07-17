# chess_tournament/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/tournament/', include('tournament.urls')),
    path('api/v1/auth/', include('authentication.urls')),
]
