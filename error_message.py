from enum import Enum

class ErrorMessage(Enum):
    MIN_MAX_NOT_NUMBERIC = "The min and max value must be numberic."
    MIN_MAX_NAGATIVE = "The min and max can only be specified as integers greater than or equal to 0."
    MIN_MAX_INVALID_RANGE = "The min value must be less than the max value."
    CHAR_COUNT_OUT_OF_RANGE = "The number of characters that can be stored must be less than the max value."