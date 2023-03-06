from error_message import ErrorMessage
from random import choice


class CharacterType:

    def __init__(self, candidate):
        self.validate_candidate(candidate)

        self._candidate = candidate
        self._min = 1
        self._max = 16
        self.characters = []

    def validate_candidate(self, candidate):
        if not candidate:
            raise ValueError(ErrorMessage.EMPTY_CANDIDATE.value)

    def validate_range(self, min, max):
        if type(min) != int or type(max) != int:
            raise ValueError(ErrorMessage.MIN_MAX_NOT_NUMBERIC.value)

        if min < 0 or max < 0:
            raise ValueError(ErrorMessage.MIN_MAX_NAGATIVE.value)

        if min > max:
            raise ValueError(ErrorMessage.MIN_MAX_INVALID_RANGE.value)

    def validate_length(self, length):
        if type(length) != int:
            raise ValueError(ErrorMessage.GENERATE_LENGTH_NOT_NUMBERIC.value)

        if length < self.min or length > self.max:
            raise ValueError(ErrorMessage.GENERATE_LENGTH_OUT_OF_RANGE.value)

    @property
    def min(self):
        return self._min

    @property
    def max(self):
        return self._max

    @property
    def filter(self):
        return self._filter

    @min.setter
    def min(self, value):
        self.validate_range(value, self._max)
        self._min = value

    @max.setter
    def max(self, value):
        self.validate_range(self._min, value)
        self._max = value

    @filter.setter
    def filter(self, value):
        self._filter = value

    def generate(self, length):
        self.validate_candidate(self._candidate)
        self.validate_length(length)

        for _ in range(length):
            self.characters.append(choice(self._candidate))
