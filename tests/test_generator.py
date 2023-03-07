import os
import string
import sys
import unittest

from password_generator import PasswordGenerator

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

    def test_set_min_and_max_of_character_type_(self) -> None:
        common_types = [
            ('uppercase', 0, 16),
            ('lowercase', 1, 12),
            ('digits', 2, 6),
            ('special', 5, 5)
        ]

        for name, min, max in common_types:
            self.generator.types[name].min = min
            self.generator.types[name].max = max

            self.assertEqual(self.generator.types[name].min, min)
            self.assertEqual(self.generator.types[name].max, max)


if __name__ == '__main__':
    unittest.main()
