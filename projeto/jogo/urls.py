from django.urls import path
from django.views.generic import RedirectView
from . import views as v

app_name = 'jogo'


urlpatterns = [
    path('', v.index, name='index'),
    path('room/', v.room_view, name='room'),
    path('gameplay', RedirectView.as_view(pattern_name='index'), name='gameplay'),
]