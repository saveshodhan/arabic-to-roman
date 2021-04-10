"""Convert Arabic numerals to Roman numerals."""

import sys

BASE_MAPPING = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX",

    10: "X",
    40: "XL",
    50: "L",
    90: "XC",

    100: "C",
    400: "CD",
    500: "D",
    900: "CM",

    1000: "M",   # think of 1000 as Ī from here onwards
    4000: "ĪV̄",
    5000: "V̄",
    9000: "ĪX̄",

    10000: "X̄",
    40000: "X̄L̄",
    50000: "L̄",
    90000: "X̄C̄",

    100000: "C̄",
    400000: "C̄D̄",
    500000: "D̄",
    900000: "C̄M̄",
    1000000: "M̄",
}


class InvalidNumeralException(Exception):
    """Custom exception."""

    pass


def convert_to_roman(num: int) -> str:
    """Convert arabic numeral to roman numeral.

    Args:
        num (int): Arabic numeral.

    Returns:
        str: Roman equivalent of `num` passed.

    Raises:
        InvalidNumeralException: This exception is raised when the `num` passes is either
            non-integer or an integer less than or equal to zero.

    Example:
        >>> print(convert_to_roman(9))
        IX
    """
    if not isinstance(num, int) or num <= 0:
        raise InvalidNumeralException(f"Invalid numeral passed == {num}")

    roman_num = ""
    for base_num in sorted(BASE_MAPPING.keys(), reverse=True):
        while num >= base_num:
            num -= base_num
            roman_num += BASE_MAPPING[base_num]
    return roman_num


if __name__ == "__main__":
    num = int(sys.argv[1])
    print(f"Roman numeral of {num} is {convert_to_roman(num)}")
