import string

from character_type import CharacterType


class PasswordGenerator:

    def __init__(self) -> None:
        self.types = dict()

        self.types["uppercase"] = CharacterType(list(string.ascii_uppercase))
        self.types["lowercase"] = CharacterType(list(string.ascii_lowercase))
        self.types["digits"] = CharacterType(list(string.digits))
        self.types["special"] = CharacterType(list(set(string.punctuation)))
