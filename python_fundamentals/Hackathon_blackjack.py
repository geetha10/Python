import random

class Card:
    def __init__(self, value:str, suit:str):
        self.type = value
        self.suit = suit

suits = ['spade', 'heart', 'club', 'diamond']
values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

deck = []
for suit in suits:
    for value in values:
        deck.append(Card(value, suit))

random.shuffle(deck)


class Participant:
    def __init__(self):
        self.hand = []
        self.points = 0

    def draw_card(self):
        self.hand.append(deck.pop(0))
    
    def discard(self):
        self.hand = []
    
    def calculate_points(self):
        self.points = 0
        for card in self.hand:
            if card.type != 'A':
                if card.type == 'J' or card.type == 'Q' or card.type == 'K':
                    self.points += 10
                else:
                    self.points += int(card.type)


class Dealer(Participant):
    def __init__(self):
        super().__init__()
    
    def deal_first_card(self, player):
        self.draw_card()
        print(f'Dealer has drawn a {self.hand[0].type}')
        player.draw_card()
        print(f'Player has drawn a {player.hand[0].type}')

    def deal_second_card(self, player):
        self.draw_card()
        player.draw_card()
        print(f'Player has drawn a {player.hand[1].type}')
    
    def reveal_card(self):
        print(f'Dealer reveals they drew a {self.hand[1].type}.')
    
    def dealer_draw(self):
        self.draw_card()
        self.calculate_points()

    def calculate_points(self):
        super()
        for card in self.hand:
            if card.type == 'A': 
                self.points += 11
                if self.points > 21:
                    self.points -= 10
        if self.points >= 17:
            return
        else:
            self.dealer_draw()

class Player(Participant):
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def hit(self):
        self.draw_card()
        print(f'You were dealt a {self.hand[-1].type}.')
        print(f'Your hand contains {len(self.hand)} cards.')
        self.hit_or_hold()
        return self
    
    def hit_or_hold(self):
        response = input("Do you wish to 'hit' or 'hold'? Type either to do so.")
        if response == 'hit':
            self.hit()
            return self
        elif response == 'hold':
            return self
        else:
            print('Your response was invalid. Please try again.')
            self.hit_or_hold()
    
    def calculate_points(self):
        for card in self.hand:
            if card.type != 'A':
                if card.type == 'J' or card.type == 'Q' or card.type == 'K':
                    self.points += 10
                else:
                    self.points += int(card.type)
            else:
                ace_choice = input('You must now decide which point value to assign to your Ace. 1 for 1, 11 for 11')
                if ace_choice == '1':
                    self.points += 1
                if ace_choice == '11':
                    self.points += 11
        print(f'Your point total is {self.points}')
        return self



def game_loop(player_name:str):
    dealer = Dealer()
    player = Player(player_name)
    dealer.deal_first_card(player)
    dealer.deal_second_card(player)
    dealer.reveal_card()
    player.hit_or_hold()
    player.calculate_points()
    if player.points >= 22:
        print('You bust. Better luck next time.')
        return
    dealer.calculate_points()
    if dealer.points >= 22:
        print ('The dealer busts. You win!')
    elif dealer.points > player.points:
        print(f'The dealer has {dealer.points} points!')
        print('The house wins!')
    else:
        print(f'The dealer has {dealer.points} points!')
        print('You win!')
    return


game_loop('brian')