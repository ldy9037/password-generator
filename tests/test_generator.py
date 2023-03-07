import os
import string
import sys
import unittest

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


if __name__ == '__main__':
    unittest.main()
