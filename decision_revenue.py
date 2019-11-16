from config import BETRAYAL, SILENCE, TWO_PLAYERS_SILENCE, TWO_PLAYERS_BETRAYAL, FIRST_PLAYER_SILENCE_SECOND_BETRAYAL, \
    FIRST_PLAYER_BETRAYAL_SECOND_SILENCE

decision_revenue = {SILENCE: {SILENCE: TWO_PLAYERS_SILENCE, BETRAYAL: FIRST_PLAYER_SILENCE_SECOND_BETRAYAL},
                    BETRAYAL: {SILENCE: FIRST_PLAYER_BETRAYAL_SECOND_SILENCE, BETRAYAL: TWO_PLAYERS_BETRAYAL}}

print(decision_revenue[SILENCE][SILENCE])
print(decision_revenue[BETRAYAL][BETRAYAL])
print(decision_revenue[SILENCE][BETRAYAL])
print(decision_revenue[BETRAYAL][SILENCE])
