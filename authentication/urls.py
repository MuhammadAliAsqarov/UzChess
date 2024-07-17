from django.urls import path
from .views import UserViewSet

urlpatterns = [
    path('register/', UserViewSet.as_view({'post': 'register', })),
    path('login/', UserViewSet.as_view({'post': 'login', })),
    path('logout/', UserViewSet.as_view({'post': 'logout', })),
]