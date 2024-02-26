import pygame

class Game:
    def __init__(self):
        self.first_hand = [[0, 0, 0, 0],
                           [0, 0, 0, 0]]
        self.second_hand = [[0, 0, 0, 0],
                            [0, 0, 0, 0]]

    def stand_card(self):
        ...

    def next_hod(self, who, position, card, row = 1):
        if who == 1:
            self.first_hand[row][position] = card
        else:
            self.second_hand[row][position] = card

