#!/usr/bin/env python3
# Imports the random module to create a random 'moves' value
import random
# Imports the time module for the print_pause function
# import time
from unicodedata import name

"""This function delays the time between print statements. """


# def print_pause(message):
#     print(message)
#     time.sleep(2)


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

    # Instance variables for Refect Player.
    my_move = random.choice(moves)
    their_move = random.choice(moves)

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


"""This class is a subclass of the Player class, assigns a random move by the player."""


class Random(Player):

    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass


"""This subclass inherits from the Player Class, as a Human Player"""


class Human(Player):

    """ This move method inherits from the Player object, and also returns human input. """

    def move(self):
        return valid_input("Rock, Paper or Scissors?\n", moves)

    def learn(self, my_move, their_move):
        pass


"""This subclass learns the move from the last round-- and then plays that move in the following round."""


class Reflect(Player):

    # Inherits from Player class, learns the opposing players move to use for it's next move.
    def move(self):
        return self.their_move

    # This method stores opponents last
    def learn(self, my_move, their_move):
        self.their_move = their_move
        self.my_move = my_move


"""This subclass cycles to the next move."""


class Cycle(Player):
    # Dunder method. Assigns the next move to the
    # possible outcome of moves.
    def __init__(self):
        self.my_next_move_index = random.randrange(3)

    # We use modulo to cycle through each move.
    # We also do not want to pick the same move twice.

    def move(self):
        my_next_move = moves[self.my_next_move_index]
        self.my_next_move_index = (self.my_next_move_index + 1) % 3
        return my_next_move


"""This function tracks what moves beat the other!"""


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
    game = Game(Human(), Cycle())
    game.play_game()
