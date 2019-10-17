from django.urls import path

from . import views

app_name = 'game'
urlpatterns = [
    path('', views.SingleGameView, name='game'),
    path('singleplayer/', views.SingleGameView, name='SingleGame'),
    path('multiplayer/', views.MultiGameView, name='MultiGame'),
    # add a history viewer view and url
]
