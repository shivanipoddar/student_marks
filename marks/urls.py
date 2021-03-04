from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('marks/', views.marks, name='marks'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]