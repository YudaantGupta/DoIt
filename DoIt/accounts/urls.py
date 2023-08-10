from django.urls import path
from . import views

urlpatterns = [
    path("signup/" , views.signup),
    path("login/" , views.login),
    path("logout/" , views.logout),
    path("profile/" , views.profile),
    path("profile/<str:username>/" , views.public)
    # path("stats/" , views.stats)
]
