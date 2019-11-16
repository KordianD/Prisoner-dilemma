from config import ALL_STRATEGIES
from strategy_factory import create_strategy
import time

start_time = time.time()
print("Start ")

for first_player_strategy in ALL_STRATEGIES:
    for second_player_strategy in ALL_STRATEGIES:
        first_player = create_strategy(first_player_strategy)
        second_player = create_strategy(second_player_strategy)

print("Stop ")
print("Time of execution {} in seconds ".format(time.time() - start_time))
