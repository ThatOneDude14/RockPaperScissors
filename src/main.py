#!/bin/bash python3
import random, sys

def playerChoice():
    print('Enter "X" to exit')
    choice = input("Choose Rock, Paper, or Scissors: ")
    choice.lower()
    if choice == 'x':
        sys.exit()
    
    return choice

def computerChoice():
    compchoice = random.randint(1,3)
    if compchoice == 1:
        choice = 'rock'
    elif compchoice == 2:
        choice = 'paper'
    else:
        choice = 'scissors'

    return choice

def compare(p, c, ps, cs):
    print()
    lost = 'You lose, computer chose {}. Play again?\n'
    won = 'You won, computer chose {}. Play again?\n'

    if p == c:
        print('Tie. Play again?\n')
        game(ps, cs)
    elif p == 'rock' and c == 'paper':
        print(lost.format(c))
        cs += 1
        score(ps, cs)
        game(ps, cs)
    elif p == 'rock' and c == 'scissors':
        print(won.format(c))
        ps += 1
        score(ps, cs)
        game(ps, cs)
    elif p == 'paper' and c == 'rock':
        print(won.format(c))
        ps += 1
        score(ps, cs)
        game(ps, cs)
    elif p == 'paper' and c == 'scissors':
        print(lost.format(c))
        cs += 1
        score(ps, cs)
        game(ps, cs)
    elif p == 'scissors' and c == 'rock':
        print(lost.format(c))
        cs += 1
        score(ps, cs)
        game(ps, cs)
    elif p == 'scissors' and c == 'paper':
        print(won.format(c))
        ps += 1
        score(ps, cs)
        game(ps, cs)
    else: 
        print("An error has occured try again\n")
        game(ps,cs)

def score(pscore, cscore):
    print(f'Score: \n Player: {pscore} \n Computer: {cscore} \n')  

def game(ps, cs):
    player = playerChoice()
    computer = computerChoice()
    compare(player, computer, ps, cs)

game(0,0)