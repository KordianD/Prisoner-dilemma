from strategies import AlwaysBetrayal, AlwaysSilence, PreviousCompetitorAnswer, AlternatelyAnswer, RandomChoice
from config import ALTERNATELY_ANSWER, ALWAYS_SILENCE, ALWAYS_BETRAYAL, PREVIOUS_COMPETITOR_ANSWER, RANDOM_CHOICE


def create_strategy(name: str):
    if name == ALWAYS_BETRAYAL:
        return AlwaysBetrayal()
    elif name == ALWAYS_SILENCE:
        return AlwaysSilence()
    elif name == PREVIOUS_COMPETITOR_ANSWER:
        return PreviousCompetitorAnswer()
    elif name == ALTERNATELY_ANSWER:
        return AlternatelyAnswer()
    elif name == RANDOM_CHOICE:
        return RandomChoice()
