#!/usr/bin/env python3

from random import randint

user_input = input()
valid_moves = ["rock", "paper", "scissors"]

while user_input not in valid_moves:
    print("invalid move, try again")
    user_input = input()

def computer_move():
    return(valid_moves[randint(0,2)])
