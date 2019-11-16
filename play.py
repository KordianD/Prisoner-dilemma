from config import ALL_STRATEGIES, NUMBER_OF_GAMES_PER_ONE_STRATEGY, NUMBER_OF_PLAYS_IN_ONE_GAME, FIRST_PLAYER_INDEX, \
    SECOND_PLAYER_INDEX
from decision_revenue import DECISION_REVENUE
from strategy_factory import create_strategy
import time

start_time = time.time()
print("Start ")

for first_player_strategy in ALL_STRATEGIES:
    for second_player_strategy in ALL_STRATEGIES:
        first_player = create_strategy(first_player_strategy)
        second_player = create_strategy(second_player_strategy)

        first_player_results = []
        second_players_results = []

        for game_number in range(NUMBER_OF_GAMES_PER_ONE_STRATEGY):

            first_player_revenue = 0
            second_player_revenue = 0

            for game in range(NUMBER_OF_PLAYS_IN_ONE_GAME):
                first_player_answer = first_player.answer()
                second_player_answer = second_player.answer()

                first_player_revenue += DECISION_REVENUE[first_player_answer][second_player_answer][FIRST_PLAYER_INDEX]
                second_player_revenue += DECISION_REVENUE[first_player_answer][second_player_answer][
                    SECOND_PLAYER_INDEX]

print("Stop ")
print("Time of execution {:.2f} in seconds ".format(time.time() - start_time))
