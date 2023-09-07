from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.utils import timezone
from .models import DisponivelPartida
from django.contrib import messages


# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')


def disponibilidade_partida(request):
    user_profile, created = DisponivelPartida.objects.get_or_create(user=request.user)
    user_profile.status = True  # Defina o status conforme necessário
    user_profile.save()
    messages.success(request, 'Solicitação registrada. Aguarde até atingir o número minimo, {}.'.format(request.user.username))
    return render(request, 'index.html')

def zerar_disponibilidade(request):
    all_users = User.objects.all()
    for signle_user in all_users:
        user_profile, created = DisponivelPartida.objects.get_or_create(user=signle_user)
        user_profile.status = False  # Defina o status conforme necessário
        user_profile.save()