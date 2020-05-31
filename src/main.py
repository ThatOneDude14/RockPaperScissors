#!/bin/bash python3
import random

def playerChoice():
    choice = input("Choose Rock, Paper, or Scissors: ")
    choice.lower()
    # if choice != 'rock' or choice != 'paper' or choice != 'scissors':
    #     print('Incorrect choice, try again\n')
        # playerChoice()
    
    return choice

def computerChoice():
    compchoice = random.randint(1,3)
    if compchoice == 1:
        choice = 'rock'
    elif compchoice == 2:
        choice = 'paper'
    else:
        choice = 'scissors'

    return 'rock'

def compare(p, c):
    lost = 'You lose, computer chose {}. Play again?\n'
    won = 'You won, computer chose {}. Play again?\n'

    if p == c:
        print('Tie. Play again?\n')
    elif p == 'rock' and c == 'paper':
        print(lost.format(c))
        game()
    elif p == 'rock' and c == 'scissors':
        print(won.format(c))
        game()
    elif p == 'paper' and c == 'rock':
        print(won.format(c))
        game()
    elif p == 'paper' and c == 'scissors':
        print(lost.format(c))
        game()
    elif p == 'scissors' and c == 'rock':
        print(lost.format(c))
        game()
    elif p == 'scissors' and c == 'paper':
        print(won.format(c))
        game()
    else: 
        print("An error has occured try again\n")
        game()
    

def game():
    player = playerChoice()
    computer = computerChoice()
    compare(player, computer)
    game()

game()