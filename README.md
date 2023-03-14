# Password Generator

This generator makes it easy to set up a new password

It supports creating:

- Passwords of any length.
- Any type of character can be used
- Strings with patterns can be used

This password generator contains numbers, lowercase letters, uppercase letters and special characters by default.

If you want to use a password that contains other types of characters or string patterns, please see the Table of Contents of Usage.

## Compatibility

This password generator has been tested on Python 3.7, 3.8, 3.9 and 3.10.

## Usage


## CharacterType Variable
| Name | Description | Type | Default |
|------|-------------|------|---------|
| candidate |  Character candidate list to be Generated. | `list` | `Constructor` |
| min |  Minimum length of list of characters to generate. | `int` | `1` |
| max |  Maximum length of list of characters to generate. | `int` | `16` |
| characters |  List of generated characters. | `list` | `[]` |

## PasswordGenerator Variable
| Name | Description | Type | Default |
|------|-------------|------|---------|
| types | Character type map to be included in password. | `dict` | <pre>{<br>  "uppercase": CharacterType(list(string.ascii_uppercase)),<br>  "lowercase": CharacterType(list(string.ascii_lowercase)),<br>  "digits": CharacterType(list(string.digits)),<br>  "special": CharacterType(list(set(string.punctuation)))<br>}</pre> |
| min |  Minimum length of list of password to generate. | `int` | `8` |
| max |  Maximum length of list of password to generate. | `int` | `16` |

## Requirements
Nothing.

## Contributing
- Code Static Analyzer ([flake8](https://github.com/pycqa/flake8)) check should pass.
- Annotations must be applied to password_generator.py and character_type.py.
- Required to write test code.
