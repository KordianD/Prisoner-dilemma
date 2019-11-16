from config import BETRAYAL, SILENCE


class AlwaysBetrayal:
    def answer(self) -> int:
        return BETRAYAL


class AlwaysSilence:
    def answer(self) -> int:
        return SILENCE


