import string

from error_message import ErrorMessage
from character_type import CharacterType


class PasswordGenerator:

    def __init__(self) -> None:
        self.types = dict()

        self._min = 8
        self._max = 16

        self.types = {
            "uppercase": CharacterType(list(string.ascii_uppercase)),
            "lowercase": CharacterType(list(string.ascii_lowercase)),
            "digits": CharacterType(list(string.digits)),
            "special": CharacterType(list(set(string.punctuation)))
        }

    def validate_range(self, min: int, max: int) -> None:
        if type(min) != int or type(max) != int:
            raise ValueError(ErrorMessage.MIN_MAX_NOT_NUMBERIC.value)

        if min < 0 or max < 0:
            raise ValueError(ErrorMessage.MIN_MAX_NAGATIVE.value)

        if min > max:
            raise ValueError(ErrorMessage.MIN_MAX_INVALID_RANGE.value)

    def validate_char_types(self) -> None:
        if not self.types:
            raise ValueError(ErrorMessage.EMPTY_CHAR_TYPE_LIST.value)

        for char_type in self.types.values():
            if type(char_type) != CharacterType:
                raise TypeError(ErrorMessage.NOT_CHARACTER_TYPE.value)

    def validate_adjust_range(self, min: int, max: int) -> None:
        if min > self.max:
            raise ValueError(ErrorMessage.GENERATOR_MAX_LT_CHAR_TYPE_MIN.value)

        if max < self.min:
            raise ValueError(ErrorMessage.GENERATOR_MIN_GT_CHAR_TYPE_MAX.value)

    @property
    def min(self) -> int:
        return self._min

    @min.setter
    def min(self, value: int) -> None:
        self.validate_range(value, self._max)
        self._min = value

    @property
    def max(self) -> int:
        return self._max

    @max.setter
    def max(self, value: int) -> None:
        self.validate_range(self._min, value)
        self._max = value

    def sum_range(self) -> tuple:
        self.validate_char_types()

        min, max = 0, 0

        for type in self.types.values():
            min += type.min
            max += type.max

        return (min, max)

    def adjust_length(self) -> None:
        min, max = self.sum_range()

        self.validate_adjust_range(min, max)
