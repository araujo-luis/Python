# Mini-project #6 - Blackjack

import simpleguitk as simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
result = ""

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}



# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print ("Invalid card: ", suit, rank)

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

# define hand class


class Hand:
    def __init__(self):
        # create Hand object
        self.hand_list = []

    def __str__(self):
        # return a string representation of a hand
        answer = ""
        for card in self.hand_list:
            answer += str(card) + " "
        return "Hand Cotains "+answer

    def add_card(self, card):
        # add a card object to a hand
        self.hand_list.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        value = 0
        isAce = False


        for card in self.hand_list:
            value+=VALUES[card.get_rank()]
            if 'A' == card.get_rank():
                isAce= True

        if isAce:
            if value + 10 <= 21:
                value+=10

        return value

    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards

        for card in self.hand_list:
            card.draw(canvas,pos)
            pos[0]+=CARD_SIZE[0]


# define deck class
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck_list = []
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank)
                self.deck_list.append(card)


    def shuffle(self):
        # shuffle the deck
        # use random.shuffle()
        random.shuffle(self.deck_list)

    def deal_card(self):
        # deal a card object from the deck
        card = self.deck_list[-1]
        self.deck_list.pop(-1)
        return card

    def count_card(self):
        return len(self.deck_list)

    def __str__(self):
        # return a string representing the deck
        cards = ""
        for card in self.deck_list:
            cards += str(card) + " "
        return "Deck Contains "+cards


#define event handlers for buttons
def deal():
    global outcome, in_play, player_hand, dealer_hand,myDeck, result, score
    outcome = "Hit or Stand?"
    result = ""
    # your code goes here

    if in_play:
        outcome = "New Deal"
        result = "You lose"
        in_play = False
        score -=1

    myDeck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()



    myDeck.shuffle()

    player_hand.add_card(myDeck.deal_card())
    dealer_hand.add_card(myDeck.deal_card())
    player_hand.add_card(myDeck.deal_card())
    dealer_hand.add_card(myDeck.deal_card())

    in_play = True

def hit():
    # replace with your code below
    global in_play, player_hand, score, result, outcome
    # if the hand is in play, hit the player

    if in_play:
        if player_hand.get_value()<=21:

            player_hand.add_card(myDeck.deal_card())

        if player_hand.get_value()>21:

            result = "You went bust and lose"
            outcome = "New Deal?"
            score-=1
            in_play = False


    # if busted, assign a message to outcome, update in_play and score

def stand():
    # replace with your code below
    global dealer_hand,myDeck, outcome, in_play,score,result
    outcome = "New Deal?"
    if in_play:
        while dealer_hand.get_value()<17:
            dealer_hand.add_card(myDeck.deal_card())


        if dealer_hand.get_value()>21:
            in_play= False

            result = "Dealer has bust"
            score+=1
        else:
            if player_hand.get_value() <= dealer_hand.get_value():

                result = "You Lose"
                score-=1
            else:


                result = "You Win"
                score+=1
            in_play=False


def draw(canvas):
    # test to make sure that card.draw works, replace with your code below

    canvas.draw_text("BlackJack",[100,100], 50, "Blue" )
    canvas.draw_text("Score: " + str(score),[400,100], 30, "Black" )
    canvas.draw_text("Dealer",[100,150], 30, "Black" )
    canvas.draw_text(result,[300,150], 30, "Black" )
    canvas.draw_text("Player",[100,380], 30, "Black" )
    canvas.draw_text(outcome,[300,380], 30, "Black" )

    pos = [120,200]
    dealer_hand.draw(canvas,pos)

    player_hand.draw(canvas, [120, 420])
    if in_play:
        card_loc = ( CARD_BACK_SIZE[0]/2,CARD_BACK_SIZE[1]/2)
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [156, 248], CARD_BACK_SIZE)


frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

dealer_hand = Hand()
player_hand = Hand()

# get things rolling
deal()
frame.start()
