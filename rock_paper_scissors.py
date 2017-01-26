"""
@ Clever Programmer
Rock paper scissors
"""
import random
# You need to have installed "SimpleGUICS2Pygame" as pip to run game locally.
# run in your terminal or cmd:
# pip install pygame (http://www.pygame.org/lofi.html)
# pip install SimpleGUICS2Pygame (https://anaconda.org/pypi/simpleguics2pygame)
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


# Global variables that all functions know about.
# DO NOT EDIT THESE GLOBAL VARIABLES
# OR YOUR GAME WILL BREAK.
COMPUTER_SCORE = 0
HUMAN_SCORE = 0
human_choice = ""
computer_choice = ""



def random_computer_choice():
    """Choose randomly for computer."""
    return random.choice (['rock', 'paper', 'scissors'])
    
    # lookup random.choice()

def choice_result(human_choice, computer_choice):
    """Return the result of who wins."""
    
    
    # DO NOT REMOVE THESE GLOBAL VARIABLE LINES.
    global COMPUTER_SCORE
    global HUMAN_SCORE
    
    if human_choice == 'rock' and computer_choice == 'paper':
        COMPUTER_SCORE = COMPUTER_SCORE + 1
    elif human_choice == 'rock' and computer_choice == 'scissors':
        HUMAN_SCORE = HUMAN_SCORE + 1
    elif human_choice == 'paper' and computer_choice == 'scissors':
        COMPUTER_SCORE = COMPUTER_SCORE + 1
    elif human_choice == 'paper' and computer_choice == 'rock':
        HUMAN_SCORE = HUMAN_SCORE + 1
    elif human_choice == 'scissors' and computer_choice == 'rock':
        COMPUTER_SCORE = COMPUTER_SCORE + 1
    elif human_choice == 'scissors' and computer_choice == 'paper':
        HUMAN_SCORE = HUMAN_SCORE + 1
    
    # based on the given human_choice and computer_choice
    # determine who won and increment their score by 1.
    # if tie, then don't increment anyone's score.
    
    # example code
    # if human_choice == 'rock' and computer_choice == 'paper':
    #    COMPUTER_SCORE = COMPUTER_SCORE + 1


# This code is for the GUI part of the game.
# Handler for mouse click on rock button.
def rock():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE
    
    human_choice = 'rock'
    computer_choice = random_computer_choice()
    choice_result(human_choice, computer_choice)

# Handler for mouse click on paper button.
def paper():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE
    
    human_choice = 'paper'
    computer_choice = random_computer_choice()
    choice_result(human_choice, computer_choice)
    
# Handler for mouse click on scissors button.
def scissors():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE
    
    human_choice = 'scissors'
    computer_choice = random_computer_choice()
    choice_result(human_choice, computer_choice)

# Handler to draw on canvas
def draw(canvas):
    
    # Draw choices
    canvas.draw_text("You: " + human_choice, [10,40], 48, "Green")
    canvas.draw_text("Comp: " + computer_choice, [10,80], 48, "Red")
        
    # Draw scores
    canvas.draw_text("Human Score: " + str(HUMAN_SCORE), [10,150], 30, "Green")
    canvas.draw_text("Comp Score: " + str(COMPUTER_SCORE), [10,190], 30, "Red")
        
    

# Create a frame and assign callbacks to event handlers
def play_rps():
    frame = simplegui.create_frame("Home", 300, 200)
    frame.add_button("Rock", rock)
    frame.add_button("Paper", paper)
    frame.add_button("Scissors", scissors)
    frame.set_draw_handler(draw)

    # Start the frame animation
    frame.start()
 
play_rps()