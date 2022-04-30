#!/usr/bin/env python3
import random

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


"""This class is for a human player."""


class HumanPlayer:
    def move(self):
        response = input("Please select: Rock, Paper, or Scissors\n").lower()
        if "rock" in response:
            return "You have selected rock."
        elif "paper" in response:
            return "You have selected paper."
        elif "scissors" in response:
            return "You have selected scissors."
        else:
            self.move()

    def learn(self, my_move, their_move):
        pass


"""This class is for a Random Player"""


class RandomPlayer:
    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass


def beats(one, two):

    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    """These class level variables keep count of score """
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

    # This logic checks which player won and displays the new score.

        if move1 == move2:
            print("This round was a tie.\n"
                  f"Player 1 Score: {self.p1_score}\n"
                  f"Player 2 score: {self.p2_score}")

        elif beats(move1, move2):

            self.p1_score += 1
            print("Player 1 wins!\n"
                  f"Player 1 Score: {self.p1_score}\n"
                  f"Player 2 score: {self.p2_score}")

        else:

            self.p2_score += 1
            print("Player 2 wins!\n"
                  f"Player 1 Score: {self.p1_score}\n"
                  f"Player 2 score: {self.p2_score}")

    def play_game(self):
        print("Welcome to the Rock Paper Scissors game!\n")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game = Game(RandomPlayer(), HumanPlayer())
    game.play_game()
