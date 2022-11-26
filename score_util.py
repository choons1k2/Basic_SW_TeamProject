from enum import Enum


class ScoreType(Enum):
    Aces = 1
    Twos = 2
    Threes = 3
    Fours = 4
    Fives = 5
    Sixes = 6
    Bonus = 7

    Chance = 8
    ThreeOfAKind = 9
    FourOfAKind = 10
    FullHouse = 11
    SmallStraight = 12
    LargeStraight = 13
    Yahtzee = 14

    def is_upper(self):
        return self.value <= 6


def is_n_of_kind(values,  n: int) -> bool:
    return any([values.count(v) >= n for v in values])


def is_full_house(values) -> bool:
    values = sorted(values)
    if is_n_of_kind(values[:3],3) and is_n_of_kind(values[3:],2):
        return True
    elif is_n_of_kind(values[:2],2) and is_n_of_kind(values[2:],3):
        return True
    else:
        return False


def is_straight(values, n: int) -> bool:
    values = sorted(values)
    for i in range(len(values) - n + 1):
        if values[i:i+n] == list(range(values[i], values[i] + n)):
            return True

    return False


def get_score(dice: list[int], score_type: ScoreType) -> int:
    if len(dice) != 5:
        raise ValueError("dice must be a list of 5 integers")

    if any([d not in range(1,7) for d in dice]):
        raise ValueError("dice must be a list of integers between 1 and 6")

    if score_type == ScoreType.Aces:
        return sum([v for v in dice if v == 1])
    elif score_type == ScoreType.Twos:
        return sum([v for v in dice if v == 2])
    elif score_type == ScoreType.Threes:
        return sum([v for v in dice if v == 3])
    elif score_type == ScoreType.Fours:
        return sum([v for v in dice if v == 4])
    elif score_type == ScoreType.Fives:
        return sum([v for v in dice if v == 5])
    elif score_type == ScoreType.Sixes:
        return sum([v for v in dice if v == 6])
    elif score_type == ScoreType.ThreeOfAKind:
        return sum(dice) if is_n_of_kind(dice,3) else 0
    elif score_type == ScoreType.FourOfAKind:
        return sum(dice) if is_n_of_kind(dice, 4) else 0
    elif score_type == ScoreType.FullHouse:
        return 25 if is_full_house(dice) else 0
    elif score_type == ScoreType.SmallStraight:
        return 30 if is_straight(dice, 4) else 0
    elif score_type == ScoreType.LargeStraight:
        return 40 if is_straight(dice, 5) else 0
    elif score_type == ScoreType.Yahtzee:
        return 50 if is_n_of_kind(dice, 5) else 0
    elif score_type == ScoreType.Chance:
        return sum(dice)
    elif score_type == ScoreType.Bonus:
        raise ValueError("Bonus is not a valid section")
    else:
        raise ValueError(f"Unknown score type {score_type}")



