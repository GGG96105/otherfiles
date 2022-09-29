import random


class Player:

    dice = 5
    current_bet = []

    def __init__(self, name, spot):
        self.name = name
        self.spot = spot
        self.hand = []
        self.create_hand()

    def get_name(self):
        return self.name

    def get_spot(self):
        return self.spot

    def create_hand(self):
        self.hand = []
        i = 0
        while i < self.dice:
            self.hand.append(random.randint(1, 6))
            i += 1

    def lose_dice(self):
        self.dice -= 1

    def get_hand(self):
        for i in self.hand:
            print(i, end=", ")
        print()

    def get_dice(self):
        print(self.dice)

    def bet(self):
        self.current_bet = []
        self.current_bet.append(int(input(f"{self.name} set a face value for your bet: ")))
        self.current_bet.append(int(input(f"{self.name} set a number value to your bet: ")))

    def get_bet(self):
        for i in self.current_bet:
            print(i, end=", ")
