import os
import sys
import unittest

from character_type import CharacterType
from error_message import ErrorMessage

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


class TestCharacterType(unittest.TestCase):

    def setUp(self):
        self.uppercase = CharacterType("uppercase")

    def test_create_with_blank_and_none_name(self):
        names = ["", None]
        expected = ErrorMessage.EMPTY_NAME.value

        for name in names:
            with self.assertRaisesRegex(ValueError, expected):
                CharacterType(name)

    def test_set_min_greater_than_max(self):
        expected = ErrorMessage.MIN_MAX_INVALID_RANGE.value

        for min in range(1, 10):
            with self.assertRaisesRegex(ValueError, expected):
                self.uppercase.min = min
                self.uppercase.max = min - 1

    def test_set_non_numberic_min_max(self):
        nums = ["123", "d", 'A', "$"]
        expected = ErrorMessage.MIN_MAX_NOT_NUMBERIC.value

        for num in nums:
            with self.assertRaisesRegex(ValueError, expected):
                self.uppercase.min = num

            with self.assertRaisesRegex(ValueError, expected):
                self.uppercase.max = num

    def test_set_negative_number_min_max(self):
        nums = [-1, -3, -11]
        expected = ErrorMessage.MIN_MAX_NAGATIVE.value

        for num in nums:
            with self.assertRaisesRegex(ValueError, expected):
                self.uppercase.min = num

            with self.assertRaisesRegex(ValueError, expected):
                self.uppercase.max = num

    def test_save_character(self):
        characters = ["a", "b", "c", "d", "e"]

        for character in characters:
            self.uppercase.save_character(character)

        self.assertListEqual(self.uppercase.characters, characters)

    def test_save_character_with_filter(self):
        characters = ["a", "B", "c", "D", "E"]
        expected = ["B", "D", "E"]

        self.uppercase.filter = lambda c: c.isupper()

        for character in characters:
            self.uppercase.save_character(character)

        self.assertListEqual(self.uppercase.characters, expected)

    def test_save_character_more_than_max(self):
        expected = ErrorMessage.CHAR_COUNT_OUT_OF_RANGE.value

        with self.assertRaisesRegex(OverflowError, expected):
            for _ in range(self.uppercase.max + 1):
                self.uppercase.save_character("A")


if __name__ == '__main__':
    unittest.main()
