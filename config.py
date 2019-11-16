SILENCE = 0
BETRAYAL = 1

FIRST_PLAYER_INDEX = 0
SECOND_PLAYER_INDEX = 1

TWO_PLAYERS_SILENCE = (3, 3)
TWO_PLAYERS_BETRAYAL = (1, 1)
FIRST_PLAYER_BETRAYAL_SECOND_SILENCE = (5, 0)
FIRST_PLAYER_SILENCE_SECOND_BETRAYAL = (0, 5)

NUMBER_OF_PLAYS_IN_ONE_GAME = 100
NUMBER_OF_GAMES_PER_ONE_STRATEGY = 10

ALWAYS_BETRAYAL = "AlwaysBetrayal"
ALWAYS_SILENCE = "AlwaysSilence"
PREVIOUS_COMPETITOR_ANSWER = "PreviousCompetitorAnswer"
ALTERNATELY_ANSWER = "AlternatelyAnswer"

ALL_STRATEGIES = [ALWAYS_BETRAYAL, ALWAYS_SILENCE, PREVIOUS_COMPETITOR_ANSWER, ALTERNATELY_ANSWER]

RESULTS_FILE = "results.txt"
