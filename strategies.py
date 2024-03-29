from config import BETRAYAL, SILENCE
import random


class AlwaysBetrayal:
    def answer(self) -> int:
        return BETRAYAL

    def set_competitor_answer(self, answer_of_competitor: int):
        pass


class AlwaysSilence:
    def answer(self) -> int:
        return SILENCE

    def set_competitor_answer(self, answer_of_competitor: int):
        pass


class PreviousCompetitorAnswer:
    def __init__(self):
        self.previous_competitor_answer = random.choice([SILENCE, BETRAYAL])

    def answer(self):
        return self.previous_competitor_answer

    def set_competitor_answer(self, answer_of_competitor: int):
        self.previous_competitor_answer = answer_of_competitor


class AlternatelyAnswer:
    def __init__(self):
        self.previous_self_answer = random.choice([SILENCE, BETRAYAL])

    def answer(self):
        if self.previous_self_answer == SILENCE:
            self.previous_self_answer = BETRAYAL
        else:
            self.previous_self_answer = SILENCE

        return self.previous_self_answer

    def set_competitor_answer(self, answer_of_competitor: int):
        pass


class RandomChoice:
    def answer(self) -> int:
        return random.choice([SILENCE, BETRAYAL])

    def set_competitor_answer(self, answer_of_competitor: int):
        pass
