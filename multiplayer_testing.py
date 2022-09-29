from main import Player
from try2 import player_creation

player_list = []
number_of_players = 2

player_creation(number_of_players, Player, player_list)

for j in player_list:
    print(j.get_name())
    j.create_hand()
    j.get_hand()

for player in player_list:
    print(player.hand)