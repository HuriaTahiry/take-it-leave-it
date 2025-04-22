"""
my_work.py
Author: Huria Tahiry   This code is designed to play a game and in this game, player has 24 box options (there are different
amount of money in each of them from $1 to $1,000,000) and in the game she/he can take any of them, and
eliminate the rest of boxes. Throughout the game the player gets some offers from the banker and is able to take that
or reject the offer.
  <-- Put your name and project description here. Also include function descriptions in your code above each function.

"""

# Function: find_unopen  The purpose of the function is to see if there is only one unopened case
# left other than the one selected by the player, and return the index of that case. I used a loop, it would return flase
# if the box is unopened and True if the box is opened.
def find_unopen(opened, player_case_num):
    sum_false = 0
    false_num = -1
    for i in range(len(opened)):
        if i != player_case_num:
            if opened[i] == False:
                sum_false += 1
                false_num = 1
    if sum_false >= 2:
        return -1
    else:
        return false_num



# Function: game_over, this function checks if there is any box unopen other than players box. If all the boxes are
# opened then the game is over. This loop checks if in the range of opened boxes there is any unopened except player's box.
#Return True if each case in the list is either open or the player's case. (my note)
def game_over(opened, player_case_num):
    sum = 0
    for i in range(len(opened)):
        if i == player_case_num:
            if opened[i]:
                sum += 1
    if sum == len(opened) -1:
        return True
    else:
        return False


# Function: get_options, This function offers any box to the player but not the players box and not the opened one.
# It returns a list of indexes corresponding to the unopened cases, excluding the player's case.
def get_options(opened, player_case_num):
    sum_false= 0
    false_num = []
    for i in range(len(opened)):
        if 1 != player_case_num and not opened[i]:
            sum_false +=1
            false_num.append(i)
    return false_num


# Function: largest_unchosen, in this funtion it indicates whether each case has been opened or not. and findthe largest
#number that remain in the game finally it returns the largest amount of money in an unopened box.
def largest_unchosen(cases, opened):
    largest = 0
    for i in range(len(opened)):
        if cases[i] > largest:
            if not opened[i]:
                largest = cases[i]
    return largest


# Function: banker_offer, this was definitely the hardest function. In this one the banker offers an amount of money
# to the player. The banker knows how much many the players has in this box. The offer is based on unopened boxes. In the
# other word it offers the average when there is fewer box but When there is a lot mostly the offer is less.
def banker_offer(cases, opened):
    unopened = [cases[i] for i in range(len(opened)) if not opened[i]]
    num_unopened = len(unopened)
    if num_unopened == 0:
        return 0
    elif num_unopened <= 4:
        ans = sum(unopened) / num_unopened
        return ans
    else:
        avg = sum(unopened) / num_unopened
        dev = avg / 2
        ans2 = avg - dev
        return ans2


if __name__ == '__main__':
    import take_it_leave_it
