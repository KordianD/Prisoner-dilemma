from config import ALL_STRATEGIES, NUMBER_OF_GAMES_PER_ONE_STRATEGY
from strategy_factory import create_strategy
import time

start_time = time.time()
print("Start ")

for first_player_strategy in ALL_STRATEGIES:
    for second_player_strategy in ALL_STRATEGIES:
        first_player = create_strategy(first_player_strategy)
        second_player = create_strategy(second_player_strategy)

        first_player_results = []
        second_players_result = []

        for game_number in range(NUMBER_OF_GAMES_PER_ONE_STRATEGY):
            pass

print("Stop ")
print("Time of execution {} in seconds ".format(time.time() - start_time))
