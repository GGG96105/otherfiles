from main import Player
from try2 import liar

wild_card = 1
p1 = Player("Player 1", 1)
p2 = Player("Player 2", 2)
players_list = [p1, p2]

while True:
    p1.create_hand()
    p2.create_hand()
    p1.get_hand()
    print()
    p2.get_hand()
    print()
    while True:
        p1.bet()
        if p1.current_bet != [0, 0]:
            pass
        else:
            if liar(p2, players_list, wild_card) == 1:
                p2.lose_dice()
                print(f"{p2.name} lost a dice! ")
                break
            else:
                p1.lose_dice()
                print(f"{p1.name} lost a dice! ")
                break

        p2.bet()
        if p2.current_bet != [0, 0]:
            pass
        else:
            if liar(p1, players_list, wild_card) == 1:
                p1.lose_dice()
                print(f"{p1.name} lost a dice! ")
                break
            else:
                p2.lose_dice()
                print(f"{p2.name} lost a dice! ")
                break

    if input("One more time?") != "n":
        continue
    else:
        break
