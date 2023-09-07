from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from ..accounts.forms import UsuarioForm
from django.urls import reverse_lazy
from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver
from ..core.models import DisponivelPartida


# Create your views here
def user_login(request):
    template_name = 'login.html'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('core:index')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
            return render(request, 'login.html')
    return render(request, template_name, {})


class CreateUser(CreateView):
    template_name = 'user_form.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('accounts:user_login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['Titulo'] = "Cadastrar novo usuario"
        context['botao'] = 'Cadastrar'
        return context

@receiver(user_logged_out)
def custom_logout_handler(sender, request, **kwargs):
    user_profile, created = DisponivelPartida.objects.get_or_create(user=request.user)
    user_profile.status = False  # Defina o status conforme necessário
    user_profile.save()
    pass


def cartas(request):
    suits = ['♥️', '♣️', '♦️', '♠️']
    cards = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
    deck = []               # deck de cartas
    player_hand = []        # guarda as cartas dos players
    nop = 9                 # numero de players

    while True:
        # Gerando o deck de cartas...
        for suit in suits:               # para cada naipe...
            for card in cards:           # sera adiconada uma carta...
                deck.append(card + suit) # via funcao 'append()'
        shuffle(deck)                    # reembaralhar
        player_hand = []
        out_cards = []

        for def_hands in range(0, nop):  # def_hands, definir maos dos players
            player_hand.append(deck.pop(0)), player_hand.append(deck.pop(0))

        x = 0
        for show in range(0, nop):       # mostrar as maos dos players
            print(f'Player{show+1}: {player_hand[x]} {player_hand[x+1]}')
            x += 2

        board = []
        board.append(deck.pop(0)), board.append(deck.pop(0)), board.append(deck.pop(0)), board.append(deck.pop(0)), board.append(deck.pop(0)) # definindo board
        print(f'{" " * 7}Board: {board[0]} {board[1]} {board[2]} {board[3]} {board[4]}')

        entrada = input() # apenas para nao entrar em loop infinito