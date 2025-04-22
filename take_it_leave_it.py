"""
Take it or Leave it Game
Parody of the "Deal or No Deal" Game Show
author: Your Elon CSC 1300 Professors

Note: students should not change anything in this file.
Run this file to play the game.
"""
import turtle
import time
import random
import my_work

def money_options(cases, picked):
    money = [cases[x] for x in range(len(cases)) if not picked[x]]
    money.sort()
    return money

# This function makes an integer into a string with commas every third digit.
def format(num):
    return "{:,}".format(num)

# Returns a shuffled version of the input list.  The input list gets destroyed
# in the process.
def shuffle(lst):
    cases = []
    num_cases = len(lst)
    for i in range(num_cases):
        rindex = random.randint(0, len(lst)-1)
        cases.append(lst.pop(rindex))
    return cases

# This function draws the suitcases and the money board
# Each suitcase is one turtle.
# The function returns a list of the turtles, in the
# same order as the suitcase numbers.
# The input is a list of positions on the money board
# for each suitcase.  The same turtle that shows suitcase
# number i makes the analogous rectangle on the money board.
def make_case_turtles(positions):
    case_turtles = []
    x = case_start_x
    y = case_start_y
    for i in range(len(cases)):
        t = turtle.Turtle()
        original_index = original.index(cases[i])
        position = positions[original_index]
        t.speed('fastest')
        t.penup()
        t.goto(position[0],position[1])
        t.pencolor("black")
        t.fillcolor("yellow")
        t.begin_fill()
        t.pendown()
        t.forward(rect_length)
        t.right(90)
        t.forward(rect_height)
        t.right(90)
        t.forward(rect_length)
        t.right(90)
        t.forward(rect_height)
        t.right(90)
        t.end_fill()
        t.penup()
        t.right(90)
        t.forward(rect_height//2)
        t.left(90)
        t.forward(rect_length//4)
        t.write(format(original[original_index]), False,font=('monaco',12,'bold'))
        t.penup()
        t.goto(x,y-5)
        t.shape('case.gif')
        t.write(str(i), False, font=('monaco',12,'bold'))
        t.goto(x,y)
        y = y - case_height
        if y <= -(window_height/2) + padding + case_height:
            y = (window_height/2) - 3*padding
            x = x + case_width + padding
        case_turtles.append(t)
    return case_turtles

# This function lets the player choose "their" case.
# That case gets relocated to the bottom center of the screen.
# The number of the player case is returned.
def get_user_case():
    num = -1
    while not (0<= num <= 24):
        num = int(turtle.numinput("Take it or Leave it", "Welcome to the game! Which case do you pick?", minval=0, maxval=24))
    case_turtles[num].undo()
    case_turtles[num].undo()
    case_turtles[num].penup()
    case_turtles[num].goto(-55,-205)
    case_turtles[num].write(str(num), False, font=('monaco',12,'bold'))
    case_turtles[num].goto(-55,-200)
    return num

# This function plays one round.
# Inputs are: How many cases have to be opened in the round (num_to_remove)
# The whole list of shuffled money amounts (cases)
# The list of which cases have been opened already (picked)
# The index of the player's suitcase (player_case_num)
# The list of turtles, one per suitcase (case_turtles)
# The function returns the banker's offer and either 't' for take the offer or 'l' for leave it.

def play_round(num_to_remove, cases, picked, player_case_num, case_turtles):
    text = "New Round \n"
    text += "Time to pick some cases!  You need to open "+ str(num_to_remove) + " this round.\n"
    for i in range(num_to_remove):
        # Get the suitcases that are still in play
        options = my_work.get_options(picked, player_case_num)    
        chosen = -1
        while chosen not in options:
            chosen = int(turtle.numinput("Take it or Leave it",
                                         text+
                                         "Which case do you want to eliminate?"))
        # Get a sorted list of the money amounts that are still in play
        money = money_options(cases, picked)
        text = ""
        if money[-1] == cases[chosen]:
            text += "Oh no! You picked the big money!\n"
        text+= "Case " + str(chosen) +" had $" + format(cases[chosen])
        # Eliminate the chosen case
        picked[chosen] = True
        case_turtles[chosen].clear()
        case_turtles[chosen].hideturtle()
        turtle.textinput("Take it or Leave it", text+"\nType any key to continue.")
        text = "You need to open "+str(num_to_remove-i-1) + " more.\n"
    # At end of round, get the banker's offer
    text = "Now let's get the banker's offer!\n"
    offer = my_work.banker_offer(cases, picked)
    text+="The banker offers you $" + format(offer)+"\n"
    reply = ""
    while reply != "t" and reply != "l":
        reply = turtle.textinput("Take it or Leave it",
                                 text+"Do you want to take the offer or leave it? Type 't' or 'l'")
    return reply, offer

# Main game code
wn = turtle.Screen()
window_length = 850
window_height = 600
rect_length = 100
rect_height = 55
case_width = 75
case_height = 55
padding = 20
case_start_x = -(window_length/2) + 3 * padding 
case_start_y = (window_height/2) - 3 * padding
moneyboard_start_x = 100 
moneyboard_start_y = (window_height//2) - 3 * padding + (rect_height//2)
offers_start_x = 0
offers_start_y = (window_height//2) - 3 * padding + (rect_height//2)
turtle.setup(width=window_length,height=window_height)
wn.title("Take it or Leave it")
wn.addshape("case.gif")

original = [1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750,
               1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]

cases = shuffle(original[:])
picked = [False]*len(cases)
positions = []
x = moneyboard_start_x
y = moneyboard_start_y
# calculate the position of each money amount on the moneyboard.
for i in range(25):
    positions.append((x,y))
    y = y - rect_height
    if y <= -(window_height//2) + padding + case_height:
        y = (window_height//2) - 3*padding + (rect_height//2)
        x = x + rect_length

offers = []
# This turtle will write down the banker's offers
offer_turtle = turtle.Turtle()
offer_turtle.penup()
offer_turtle.goto(0, window_height//2-padding)
offer_turtle.hideturtle()

# These turtles draw the suitcases
case_turtles = make_case_turtles(positions)
user_case = get_user_case()
num_to_remove = 6
reply = 'l'
while reply == 'l' and (picked.count(False)!=2):
    (reply, offer) = play_round(num_to_remove, cases, picked, user_case, case_turtles)
    if(offers == []):
        offer_turtle.pendown()
        offer_turtle.write("Banker Offers:", False,font=('monaco',12,'bold'))
        offer_turtle.penup()
        (x_pos, y_pos) = offer_turtle.pos()
        offer_turtle.goto(x_pos, y_pos - padding)
    offers.append(offer)
    offer_turtle.pendown()
    offer_turtle.write("$"+format(offer), False,font=('monaco',12,'bold'))
    offer_turtle.penup()
    (x_pos, y_pos) = offer_turtle.pos()
    offer_turtle.goto(x_pos, y_pos - padding)
    num_to_remove = max(num_to_remove-1, 1)
# When there are only 2 cases left the player gets to switch if they want to.
if (picked.count(False)==2):
    unopened = my_work.find_unopen(picked, user_case)
    text = "There's only one unopened case left besides yours, case "+str(unopened)+"\n"
    reply = ''
    while reply != 's' and reply != 'k':
        reply = turtle.textinput("Take it or Leave it",
            text + "Do you want to switch to that case or keep your original case?\n"
                                 +"Type 's' to switch or 'k' to keep")
    discard = unopened
    if reply == 's':
        discard = user_case
        user_case = unopened
    picked[discard] = True
    case_turtles[discard].clear()
    case_turtles[discard].hideturtle()
    text = "The case you did not choose contained: $"+format(cases[discard])+"\n"
    turtle.textinput("Take it or Leave it",text + "Type any key to continue.")
if my_work.game_over(picked, user_case):
    text = "The game is over!  You won $"+format(cases[user_case])
else:
    text = "You take the offer! But could you have done better? \n"
    text += "You win $" + format(offer) + "\n"
    best_not_picked = my_work.largest_unchosen(cases, picked)
    index_best = cases.index(best_not_picked)
    text += "The $" + format(best_not_picked) + " was in case " +str(index_best)+"\n"
    text += "Your case,"+ str(user_case)+ ",had $"+ format(cases[user_case])
turtle.textinput("Take it or Leave it",text + "\nType any key to end the game.")
turtle.done()
turtle.bye()
