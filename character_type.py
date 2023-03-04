from error_message import ErrorMessage


class CharacterType:
    def __init__(self, name):
        self.validate(name)

        self.name = name
        self._min = 1
        self._max = 16
        self._filter = lambda c: True
        self.characters = []

    def validate(self, name):
        if not name:
            raise ValueError(ErrorMessage.EMPTY_NAME.value)

    def validate_range(self, min, max):
        if type(min) != int or type(max) != int:
            raise ValueError(ErrorMessage.MIN_MAX_NOT_NUMBERIC.value)

        if min < 0 or max < 0:
            raise ValueError(ErrorMessage.MIN_MAX_NAGATIVE.value)

        if min > max:
            raise ValueError(ErrorMessage.MIN_MAX_INVALID_RANGE.value)

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

    def save_character(self, character):
        if self._filter(character):
            if len(self.characters) >= self.max:
                raise OverflowError(ErrorMessage.CHAR_COUNT_OUT_OF_RANGE.value)

            self.characters.append(character)
