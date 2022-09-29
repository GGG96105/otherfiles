# def liar(a, wild_card):
#     checked_hand = []
#     if wild_card == 1:
#         for i in a.hand:
#             if i == 1:
#                 checked_hand.append(a.current_bet[0])
#             else:
#                 checked_hand.append(i)
#     if a.current_bet[1] <= checked_hand.count(a.current_bet[0]):
#         return 0
#         # if telling the truth
#     else:
#         return 1
#         # if lying


def player_creation(number_of_players, class_used, player_list):
    for i in range(number_of_players):
        globals()["w" + str(i)] = class_used(f'Player {i + 1}', i + 1)
        player_list.append(globals()["w" + str(i)])


def liar(a, player_list, wild_card):
    checked_hand = []
    to_be_checked = []

    for player in player_list:
        for n in player.hand:
            to_be_checked.append(n)
    if wild_card == 1:
        for i in to_be_checked:
            if i == 1:
                checked_hand.append(a.current_bet[0])
            else:
                checked_hand.append(i)
    else:
        for i in to_be_checked:
            checked_hand.append(i)
    if a.current_bet[1] <= checked_hand.count(a.current_bet[0]):
        print(1)
        for i in to_be_checked:
            print(i, end=" ")
        print()
        print(2)
        for i in checked_hand:
            print(i, end=' ')
        return 0
        # if telling the truth
    else:
        print(1)
        for i in to_be_checked:
            print(i, end=" ")
        print()
        print(2)
        for i in checked_hand:
            print(i, end=' ')
        return 1
        # if lying
