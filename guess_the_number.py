# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

secret_number = random.randrange(0, 1000)
tries = 7

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    range100()
    
    # remove this when you add your code    
    pass


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number, tries
    secret_number = random.randrange(0, 100)
    global tries
    tries = 7
    print " "
    print "New game. Range is from 0 to 100"
    print "Nomber of remaining guesses is", tries
   

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number, tries 
    secret_number = random.randrange(0, 1000)
    print " "
    print "New game. Range is from 0 to 1000"
    global tries
    tries = 10
    print "Nomber of remaining guesses is", tries
    
    
def input_guess(guess):
    # main game logic goes here	
    print " "
    guess = int(guess)    
    print "Guess was", guess
    global tries
    tries -= 1
    print "Nomber of remaining guesses is", tries
    
    if tries > 0:
        if guess > secret_number:
            print "Lower!"
        elif guess < secret_number:
            print "Higher!"
        else:
            print "Correct!"
            new_game()
    else:
        if guess == secret_number:
            print "Correct!"
        else:
            print "You ran out of guesses. The number was", secret_number
       
        new_game()
        return
      
     
    if tries == 0:
        print " "
        print "You ran out of guesses.  The number was", secret_number
        new_game()
        return
    
# create frame
frame = simplegui.create_frame("Guess the number",200,200)

# register event handlers for control elements and start frame
frame.add_button("Range is (0, 100]", range100, 200)
frame.add_button("Range is (0, 1000]", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)

# call new_game 
new_game()
frame.start()

# always remember to check your completed program against the grading rubric
