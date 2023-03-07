import os
import string
import sys
import unittest

from password_generator import PasswordGenerator

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


class TestPasswordGenerator(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_generator_contains_common_character_type(self):
        generator = PasswordGenerator()

        common_types = [
            ('uppercase', list(string.ascii_uppercase)),
            ('lowercase', list(string.ascii_lowercase)),
            ('digits', list(string.digits)),
            ('special', list(set(string.punctuation)))
        ]

        for name, candidate in common_types:
            self.assertListEqual(generator.types[name].candidate, candidate)


if __name__ == '__main__':
    unittest.main()
