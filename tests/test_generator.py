import os
import string
import sys
import unittest
import random

from password_generator import PasswordGenerator
from error_message import ErrorMessage

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


class TestPasswordGenerator(unittest.TestCase):

    def setUp(self) -> None:
        self.generator = PasswordGenerator()

    def test_generator_contains_common_character_type(self) -> None:
        common_types = [
            ('uppercase', list(string.ascii_uppercase)),
            ('lowercase', list(string.ascii_lowercase)),
            ('digits', list(string.digits)),
            ('special', list(set(string.punctuation)))
        ]

        for name, candidate in common_types:
            self.assertListEqual(
                self.generator.types[name].candidate, candidate)

    def test_set_min_greater_than_max(self):
        expected = ErrorMessage.MIN_MAX_INVALID_RANGE.value

        for min in range(1, 10):
            with self.assertRaisesRegex(ValueError, expected):
                self.generator.min = min
                self.generator.max = min - 1

    def test_set_non_numberic_min_max(self) -> None:
        nums = ["123", "d", 'A', "$"]
        expected = ErrorMessage.MIN_MAX_NOT_NUMBERIC.value

        for num in nums:
            with self.assertRaisesRegex(ValueError, expected):
                self.generator.min = num

            with self.assertRaisesRegex(ValueError, expected):
                self.generator.max = num

    def test_set_negative_number_min_max(self) -> None:
        nums = [-1, -3, -11]
        expected = ErrorMessage.MIN_MAX_NAGATIVE.value

        for num in nums:
            with self.assertRaisesRegex(ValueError, expected):
                self.generator.min = num

            with self.assertRaisesRegex(ValueError, expected):
                self.generator.max = num

    def test_sum_char_type_length_range(self) -> None:
        expected_min = 0
        expected_max = 0

        for type in self.generator.types.values():
            type.min = random.randrange(0, 5)
            expected_min += type.min

            type.max = random.randrange(5, 9)
            expected_max += type.max

        self.assertTupleEqual(
            self.generator.sum_range(),
            (expected_min, expected_max))

    def test_sum_char_type_length_range_with_empty_types(self) -> None:
        expected = ErrorMessage.EMPTY_CHAR_TYPE_LIST.value
        self.generator.types = []

        with self.assertRaisesRegex(ValueError, expected):
            self.generator.sum_range()

    def test_sum_char_type_length_range_with_other_types(self) -> None:
        expected = ErrorMessage.NOT_CHARACTER_TYPE.value
        other_types = ["str", 1, [1, 2], {"test": "t"}]

        for other_type in other_types:
            self.generator.types["none_character_type"] = other_type

            with self.assertRaisesRegex(TypeError, expected):
                self.generator.sum_range()


if __name__ == '__main__':
    unittest.main()
