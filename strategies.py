from config import BETRAYAL, SILENCE


class AlwaysBetrayal:
    def answer(self, answer_of_competitor) -> int:
        return BETRAYAL


class AlwaysSilence:
    def answer(self, answer_of_competitor) -> int:
        return SILENCE


class PreviousCompetitorAnswer:
    def __init__(self):
        self.previous_competitor_answer = SILENCE

    def answer(self, answer_of_competitor):
        actual_answer = self.previous_competitor_answer
        self.previous_competitor_answer = answer_of_competitor
        return actual_answer
