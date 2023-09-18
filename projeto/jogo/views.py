from django.shortcuts import render, redirect
from django.contrib import messages
import random
import string

# Create your views here.


class Cheap:
    cheap = []
    def __init__(self): 
        suites = ['♥️', '♣️', '♦️', '♠️']
        values = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']
        self.cheap = [f'{suite}{value}' for suite in suites for value in values]
    
    def distribute_cards(self, num_cards, num_players):
        total_number_cards = num_cards * num_players
        if total_number_cards > len(self.cheap):
            raise ValueError("Não há cartas suficientes no baralho para distribuir para todos os jogadores.")

        random.shuffle(self.cheap) # embaralha o deck
        hands_players = [[] for _ in range(num_players)]
        for i in range(num_cards):
            for j in range(num_players):
                card = self.cheap.pop()
                hands_players[j].append(card)
        return hands_players




def index(request):
    num_of_players = 6
    num_of_cards = 6
    cheap = Cheap()
    hands_plays = cheap.distribute_cards(num_of_cards, num_of_players)
    return render(request, 'gameshow.html', {'hands_plays': hands_plays})


def room_view(request):
    return render(request, 'room.html')



