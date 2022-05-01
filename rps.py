#!/usr/bin/env python3
# Imports the random module to create a random 'moves' value
import random

"""This function validates user input"""


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print(f'The option "{option}" is invalid. Try again!')


"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


"""This class is a subclass of the Player class, assigns a Random Player"""


class RandomPlayer(Player):

    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass


"""This subclass inherits from the Player Class, as a Human Player"""


class HumanPlayer(Player):

    def move(self):

        response = valid_input(
            "Please write: Rock, Paper or Scissors\n")
        if response == 'rock':
            print("You've selected Rock.")
        elif response == 'paper':
            print("You've selected paper")
        elif response == 'scissors':
            print("You've selected scissors.")

    def learn(self, my_move, their_move):
        pass


def beats(one, two):

    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    """Class level variables for score count"""
    p1_score = 0
    p2_score = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        # Instance level variables for score keeping.
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
    # This logic checks which player won/tie and tracks the score.
        if move1 == move2:
            print("This round is a tie!\n"
                  f"Player 1 Score: {self.p1_score}\n"
                  f"Player 2 Score: {self.p2_score}")

        elif beats(move1, move2):
            self.p1_score += 1
            print("Player 1 Wins!\n"
                  f"Player 1 Score: {self.p1_score}\n"
                  f"Player 2 Score: {self.p2_score}")

        if beats(move2, move1):
            self.p2_score += 1
            print("Player 2 wins\n"
                  f"Player 1 Score: {self.p1_score}\n"
                  f"Player 2 Score: {self.p2_score}")

    def play_game(self):
        print("Welcome to the Rock Paper Scissors game!\n")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game = Game(Player(), HumanPlayer())
    game.play_game()
