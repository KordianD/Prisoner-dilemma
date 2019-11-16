from config import ALL_STRATEGIES, NUMBER_OF_GAMES_PER_ONE_STRATEGY, NUMBER_OF_PLAYS_IN_ONE_GAME, FIRST_PLAYER_INDEX, \
    SECOND_PLAYER_INDEX
from utils import save_results_to_file, get_revenue_for_answer, remove_results_file_if_exists
from strategy_factory import create_strategy
import time

start_time = time.time()
print("Start ")

remove_results_file_if_exists()

for first_player_strategy in ALL_STRATEGIES:
    for second_player_strategy in ALL_STRATEGIES:
        first_player = create_strategy(first_player_strategy)
        second_player = create_strategy(second_player_strategy)

        first_player_results = []
        second_player_results = []

        for game_number in range(NUMBER_OF_GAMES_PER_ONE_STRATEGY):

            first_player_revenue = 0
            second_player_revenue = 0

            for game in range(NUMBER_OF_PLAYS_IN_ONE_GAME):
                first_player_answer = first_player.answer()
                second_player_answer = second_player.answer()

                first_player_revenue += get_revenue_for_answer(first_player_answer, second_player_answer,
                                                               FIRST_PLAYER_INDEX)
                second_player_revenue += get_revenue_for_answer(first_player_answer, second_player_answer,
                                                                SECOND_PLAYER_INDEX)

                first_player.set_competitor_answer(second_player_answer)
                second_player.set_competitor_answer(first_player_answer)

            first_player_results.append(first_player_revenue)
            second_player_results.append(second_player_revenue)

        save_results_to_file(first_player_strategy, second_player_strategy, first_player_results, second_player_results)

print("Stop ")
print("Time of execution {:.2f} in seconds ".format(time.time() - start_time))
