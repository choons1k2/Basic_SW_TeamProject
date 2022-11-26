from abc import abstractmethod
from score_util import get_score, ScoreType


class Section:
    def __init__(self, dice: list[int], score_type: ScoreType):
        self.dice = dice
        self.score_type = score_type

    def get_score(self):
        if self.score_type.is_upper():
            raise NotImplementedError
        else:
            return get_score(self.dice, self.score_type)


class Board:
    def __init__(self, size):
        self._size = size
        self._section_dict = {}

    @property
    def size(self):
        return self._size

    def add_section(self, section: Section):
        if section.score_type in self._section_dict:
            raise ValueError(f"Section {section.score_type} already exists")
        if len(self._section_dict) >= self._size:
            raise ValueError("Board is full")
        if not self.is_valid_type(section.score_type):
            raise ValueError(f"Invalid score type {section.score_type}")

        self._section_dict[section.score_type] = section

    @abstractmethod
    def get_score(self):
        pass

    @abstractmethod
    def is_valid_type(self, score_type: ScoreType):
        pass


class TopBoard(Board):
    pass


class BottomBoard(Board):
    def __init__(self):
        super().__init__(7)

    def get_score(self):
        return sum([section.get_score() for section in self._section_dict.values()])

    def is_valid_type(self, score_type: ScoreType):
        return not score_type.is_upper()

if __name__ == "__main__":
    bottom_board = BottomBoard()
    bottom_board.add_section(Section([1, 2, 3, 4, 5], ScoreType.ThreeOfAKind))
    bottom_board.add_section(Section([1, 2, 3, 4, 5], ScoreType.FourOfAKind))
    bottom_board.add_section(Section([1, 2, 3, 4, 5], ScoreType.FullHouse))
    bottom_board.add_section(Section([1, 2, 3, 4, 5], ScoreType.SmallStraight))
    bottom_board.add_section(Section([1, 2, 3, 4, 5], ScoreType.LargeStraight))
    bottom_board.add_section(Section([1, 2, 3, 4, 5], ScoreType.Yahtzee))
    bottom_board.add_section(Section([1, 2, 3, 4, 5], ScoreType.Chance))
    print(bottom_board.get_score())
