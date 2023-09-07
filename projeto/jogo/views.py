from django.shortcuts import render

# Create your views here.


class Cheap:
    cheap = []
    def __init__(self): 
        suites = ['♥️', '♣️', '♦️', '♠️']
        values = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']
        self.cheap = [f'{value}{suite}' for suite in suites for value in values]
    
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
    return render(request, 'gameshow.html')

