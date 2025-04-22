"""
Tester for my_work.py, for the "Take it or Leave it" game
Assignment on list algorithms
@author: Elon CSC 1300 Professors
"""

import my_work
import random

def test_find_unopen():
    # Check for lists of 1 False value - 1 Unopen case
    for i in range(10):
        size = random.randint(5,9)
        target = random.randint(0,size-1)
        case_list = [True]*size
        case_list[target] = False
        for num in range(size):
            if num != target:
                original = case_list[:]
                your_answer = my_work.find_unopen(case_list,num)
                if not check_answer('find_unopen', [case_list, num], your_answer, target,[original],[case_list]):
                    return False

   # Check for lists of 2 False values
    for i in range(10):
        size = random.randint(5,9)
        target = random.randint(0,size-1)
        mycase = target
        while mycase == target:
            mycase = random.randint(0, size-1)
        case_list = [True]*size
        case_list[target] = False
        case_list[mycase] = False
        original = case_list[:]
        your_answer = my_work.find_unopen(case_list, mycase)
        if not check_answer('find_unopen', [case_list, mycase], your_answer, target, [original], [case_list]):
            return False

    # Check for lists of 0 False
    cases = [True]*20
    original = cases[:]
    your_answer = my_work.find_unopen(cases, 5)
    if not check_answer('find_unopen', [cases, 5], your_answer, -1, [original], [cases]):
        return False

    # Check for lists of 3+ Falses
    for i in range(10):
        size = random.randint(7,12)
        case1 = random.randint(0,size-1)
        case2 = case1
        while case2 == case1:
            case2 = random.randint(0, size-1)
        case3 = case2
        while case3 == case2 or case3 == case1:
            case3 = random.randint(0, size-1)
        case_list = [True]*size
        case_list[case1] = False
        case_list[case2] = False
        case_list[case3] = False
        moreTrues = random.randint(0,9)
        for i in range(moreTrues):
            rand = random.randint(0,len(case_list)-1)
            case_list[rand] = False
        mycase = random.randint(0, len(case_list)-1)
        original = case_list[:]
        your_answer = my_work.find_unopen(case_list, mycase)
        if not check_answer('find_unopen', [case_list, mycase], your_answer, -1, [original], [case_list]):
            return False
    return True

def test_game_over():
    # Check for lists of 1 Unopened value
    # If the unopened case is the player case, should return True, else False
    for i in range(10):
        size = random.randint(5, 9)
        target = random.randint(0, size - 1)
        case_list = [True] * size
        case_list[target] = False
        for num in range(size):
            if num != target:
                original = case_list[:]
                your_answer = my_work.game_over(case_list, num)
                if not check_answer('game_over', [case_list, num], your_answer, False, [original], [case_list]):
                    return False
            else:
                original = case_list[:]
                your_answer = my_work.game_over(case_list, num)
                if not check_answer('game_over', [case_list, num], your_answer, True, [original], [case_list]):
                    return False

    # Check for lists of 2 False values
    for i in range(10):
        size = random.randint(5, 9)
        target = random.randint(0, size - 1)
        mycase = target
        while mycase == target:
            mycase = random.randint(0, size - 1)
        case_list = [True] * size
        case_list[target] = False
        case_list[mycase] = False
        original = case_list[:]
        your_answer = my_work.game_over(case_list, mycase)
        if not check_answer('game_over', [case_list, mycase], your_answer, False, [original], [case_list]):
            return False

    # Check for lists of 0 False Values
    cases = [True] * 20
    original = cases[:]
    your_answer = my_work.game_over(cases, 5)
    if not check_answer('game_over', [cases, 5], your_answer, True, [original], [cases]):
        return False

    # Check for lists of 3+ Trues
    for i in range(10):
        size = random.randint(7, 12)
        case1 = random.randint(0, size - 1)
        case2 = case1
        while case2 == case1:
            case2 = random.randint(0, size - 1)
        case3 = case2
        while case3 == case2 or case3 == case1:
            case3 = random.randint(0, size - 1)
        case_list = [True] * size
        case_list[case1] = False
        case_list[case2] = False
        case_list[case3] = False
        moreTrues = random.randint(0, 9)
        for i in range(moreTrues):
            rand = random.randint(0, len(case_list) - 1)
            case_list[rand] = False
        mycase = random.randint(0, len(case_list) - 1)
        original = case_list[:]
        your_answer = my_work.game_over(case_list, mycase)
        if not check_answer('game_over', [case_list, mycase], your_answer, False, [original], [case_list]):
            return False
    return True

def test_get_options():
    # General random tests
    for i in range(10):
        size = random.randint(5, 9)
        player = random.randint(0, size - 1)
        picked = []
        answer = []
        for c in range(size):
            if random.random() < .5:
                case_open = False
            else:
                case_open = True
            picked.append(case_open)
            if case_open == False and c != player:
                answer.append(c)
        original = picked[:]
        your_answer = my_work.get_options(picked, player)
        if not check_answer('get_options', [picked, player], your_answer, answer, [original], [picked]):
            return False
    # All or nothing tests. = ALL TRUE, player true
    size = random.randint(5, 9)
    player = random.randint(0, size - 1)
    picked = [True] * size
    original = picked[:]
    your_answer = my_work.get_options(picked, player)
    if not check_answer('get_options', [picked, player], your_answer, [], [original], [picked]):
            return False
    # All or nothing tests. = ALL TRUE, player false
    picked[player] = False
    original = picked[:]
    your_answer = my_work.get_options(picked, player)
    if not check_answer('get_options', [picked, player], your_answer, [], [original], [picked]):
        return False
    # All or nothing tests. = ALL FALSE, player false
    size = random.randint(5, 9)
    player = random.randint(0, size - 1)
    picked = [False] * size
    original = picked[:]
    answer = [i for i in range(size) if i != player]
    your_answer = my_work.get_options(picked, player)
    if not check_answer('get_options', [picked, player], your_answer, answer, [original], [picked]):
            return False
    # All or nothing tests. = ALL FALSE, player true
    picked[player] = True
    original = picked[:]
    your_answer = my_work.get_options(picked, player)
    if not check_answer('get_options', [picked, player], your_answer, answer, [original], [picked]):
        return False
    return True

def make_random():
    cases = []
    picked = []
    for i in range(10):
        cases.append(random.randint(-5,10))
        if random.random() < .5:
            picked.append(True)
        else:
            picked.append(False)
    return(cases, picked)

def test_biggest():
    # Need: cases, opened
    # All open except small case
    for target in range(10):
        cases = [10]*10
        picked = [True]*10
        cases[target] = 2
        picked[target] = False
        original_cases = cases[:]
        original_picked = picked[:]
        your_answer = my_work.largest_unchosen(cases, picked)
        if not check_answer('largest_unchosen', [cases, picked], your_answer, 2,
                            [original_cases, original_picked], [cases, picked]):
            return False
    # Random Trials
    for trial in range(10):
        cases, picked = make_random()
        target = random.randint(0, len(cases)-1)
        answer = random.randint(11,20)
        cases[target] = answer
        picked[target] = False
        original_cases = cases[:]
        original_picked = picked[:]
        your_answer = my_work.largest_unchosen(cases, picked)
        if not check_answer('largest_unchosen', [cases, picked], your_answer, answer,
                            [original_cases, original_picked], [cases, picked]):
            return False
        # Try adding other big open cases
        more = random.randint(1,3)
        for i in range(more):
            another = target
            while another == target:
                another = random.randint(0, len(cases) - 1)
            cases[another] = 100
            picked[another] = True
        original_cases = cases[:]
        original_picked = picked[:]
        your_answer = my_work.largest_unchosen(cases, picked)
        if not check_answer('largest_unchosen', [cases, picked], your_answer, answer,
                           [original_cases, original_picked], [cases, picked]):
            return False
    return True
def check_answer(fun_name, inputs, your_answer,my_answer, dont_change_original,dont_change_after):
    for i in range(len(dont_change_original)):
        if not unchanged(dont_change_original[i], dont_change_after[i]):
            print_oops_change(fun_name, inputs,dont_change_original[i], dont_change_after[i])
            return False
    if your_answer != my_answer:
        print_wrong_answer(fun_name, inputs, your_answer, my_answer)
        return False
    return True

def print_oops_change(fun_name, inputs, input_orig, input_changed):
    print("INCORRECT: For function: ",fun_name)
    print("Arguments are: ", inputs)
    print("Some list arguments changed as a result of calling the function.")
    print("Before function:",input_orig)
    print("After function:", input_changed)

def print_wrong_answer(fun_name, inputs, your_answer, my_answer):
    print("INCORRECT: For function: ",fun_name)
    print("Arguments are: ", inputs)
    print("Your answer was:", your_answer)
    print("But should have been:", my_answer)

def unchanged(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            return False
    return True

def perform_tests():
    print("Testing: Find Unopen")
    if test_find_unopen():
        print("******** All tests Passed")
    print("Testing: Game Over")
    if test_game_over():
        print("******** All tests Passed")
    print("Testing: Get Options")
    if test_get_options():
        print("******** All tests Passed")
    print("Testing: Largest Unchosen")
    if test_biggest():
        print("******** All tests Passed")

if __name__ == "__main__":
    perform_tests()


