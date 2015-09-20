# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console



# in code sckuptor
#   http://www.codeskulptor.org/#user40_zqw9Kxhutv_1.py
import simpleguitk as simplegui
import random
import math

secret_number = 0
num_range = 100
atempt = 0
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, num_range, atempt
    secret_number = random.randrange(0, num_range)
    atempt= math.ceil( math.log(num_range + 1) / math.log(2))
    print(atempt)
    atempt = int(atempt)

    print()
    print ("New game. Game is from 0 to",num_range)
    print ("Number of remaining guesses is ",atempt)
    marco.start()



# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global num_range
    num_range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global num_range
    num_range = 1000
    new_game()

def input_guess(guess):
    # main game logic goes here
    global secret_number,atempt
    atempt = atempt-1
    print()
    if atempt==0:
        print ("You lose")
        new_game()
        return

    guess=int(guess)
    print ("Guess was",guess)
    print ("Number of remaining guesses is ",atempt)
    if guess == secret_number:
        print ("Corret!")
        new_game()
    elif guess < secret_number:
        print ("Higher")
    else:
        print ("Lower")



# create frame
marco = simplegui.create_frame("Guess the number",200,200)

# register event handlers for control elements and start frame
marco.add_button("Range of [0,100) ", range100, 200)
marco.add_button("Range of [0,1000) ", range1000, 200)
marco.add_input("Enter a Guess", input_guess, 100)


# call new_game
new_game()


# always remember to check your completed program against the grading rubric
