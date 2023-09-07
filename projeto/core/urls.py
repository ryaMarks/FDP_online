from django.urls import path

from ..core import views as v

app_name = 'core'


urlpatterns = [
    path('', v.index, name='index'),
    path('disponivel_partida/', v.disponibilidade_partida, name='disponivel_partida'),
]