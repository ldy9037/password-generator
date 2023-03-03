import unittest
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from character_type import CharacterType

class TestCharacterType(unittest.TestCase):
    
    def setUp(self):
        self.uppercase = CharacterType("uppercase")

    def test_create_with_blank_and_none_name(self):
        names = ["", None]

        for name in names:
            with self.assertRaisesRegex(ValueError, "You cannot specify an empty and None value for the name property."):
                CharacterType(name)

    def test_set_min_greater_than_max(self):
        for min in range(1, 10): 
            with self.assertRaisesRegex(ValueError, "The min value must be less than the max value."):
                self.uppercase.min = min
                self.uppercase.max = min - 1 

    def test_set_non_numberic_min_max(self):
        nums = ["123", "d", 'A', "$"]
        expected_message = "The min and max value must be numberic."

        for num in nums: 
            with self.assertRaisesRegex(ValueError, expected_message):
                self.uppercase.min = num
            
            with self.assertRaisesRegex(ValueError, expected_message):
                self.uppercase.max = num

    def test_set_negative_number_min_max(self):
        nums = [-1, -3, -11]
        expected_message = "The min and max can only be specified as integers greater than or equal to 0."

        for num in nums: 
            with self.assertRaisesRegex(ValueError, expected_message):
                self.uppercase.min = num
            
            with self.assertRaisesRegex(ValueError, expected_message):
                self.uppercase.max = num

    def test_save_character(self):
        characters = ["a", "b", "c", "d", "e"]

        for character in characters:
            self.uppercase.save_character(character)

        self.assertListEqual(self.uppercase.characters, characters)

    def test_save_character_with_filter(self):
        characters = ["a", "B", "c", "D", "E"]
        self.uppercase.filter = lambda c : c.isupper()

        for character in characters:
            self.uppercase.save_character(character)

        self.assertListEqual(self.uppercase.characters, ["B", "D", "E"])

    def test_save_character_more_than_max(self): 
        expected_message = "The number of characters that can be stored must be less than the max value."

        with self.assertRaisesRegex(OverflowError, expected_message):
            for _ in range(self.uppercase.max + 1):
                self.uppercase.save_character("A")
        
if __name__ == '__main__':
    unittest.main()