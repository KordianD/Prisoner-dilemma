from config import RESULTS_FILE
from decision_revenue import DECISION_REVENUE
import os


def save_results_to_file(first_player_strategy, second_player_strategy, first_player_results, second_players_results):
    first_player_average_score = sum(first_player_results) / len(first_player_results)
    second_player_average_score = sum(second_players_results) / len(second_players_results)

    with open(RESULTS_FILE, 'a+') as file:
        file.write(
            "{}, {}, {}, {}\n".format(first_player_strategy, str(first_player_average_score),
                                      second_player_strategy,
                                      str(second_player_average_score)))


def get_revenue_for_answer(first_player_answer, second_player_answer, player_index):
    return DECISION_REVENUE[first_player_answer][second_player_answer][player_index]


def remove_results_file_if_exists():
    if os.path.isfile(RESULTS_FILE):
        os.remove(RESULTS_FILE)
