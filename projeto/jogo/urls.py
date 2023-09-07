from django.urls import path
from . import views as v

app_name = 'jogo'


urlpatterns = [
    path('', v.index, name='index'),
]