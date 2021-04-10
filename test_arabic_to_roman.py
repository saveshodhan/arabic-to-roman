"""Test cases."""

from arabic_to_roman import InvalidNumeralException, convert_to_roman

import pytest


def make_fixture_params(case):
    """Create iterable fixture."""
    test_data = {
        "good": [
            [9, "IX"],
            [18, "XVIII"],
            [270, "CCLXX"],
            [3600, "MMMDC"],
            [45000, "X̄L̄V̄"],
            [540000, "D̄X̄L̄"],
            [6300000, "M̄M̄M̄M̄M̄M̄C̄C̄C̄"],
            [9, "IX"],
            [99, "XCIX"],
            [999, "CMXCIX"],
            [9999, "ĪX̄CMXCIX"],
            [99999, "X̄C̄ĪX̄CMXCIX"],
            [999999, "C̄M̄X̄C̄ĪX̄CMXCIX"],
            [9999999, "M̄M̄M̄M̄M̄M̄M̄M̄M̄C̄M̄X̄C̄ĪX̄CMXCIX"],
            [4, "IV"],
            [44, "XLIV"],
            [444, "CDXLIV"],
            [4444, "ĪV̄CDXLIV"],
            [44444, "X̄L̄ĪV̄CDXLIV"],
            [444444, "C̄D̄X̄L̄ĪV̄CDXLIV"],
            [4444444, "M̄M̄M̄M̄C̄D̄X̄L̄ĪV̄CDXLIV"],
        ],
        "bad": [
            [0, "Invalid numeral passed == 0"],
            [-1, "Invalid numeral passed == -1"],
            [1.5, "Invalid numeral passed == 1.5"],
            ["foo", "Invalid numeral passed == foo"],
        ]
    }
    return test_data[case]


@pytest.fixture(params=make_fixture_params("good"), ids=lambda x: f"num == {x[0]}")
def good_data(request):
    """Test fiture."""
    yield request.param


@pytest.fixture(params=make_fixture_params("bad"), ids=lambda x: f"num == {x[0]}")
def bad_data(request):
    """Test fiture."""
    yield request.param


@pytest.mark.good_case
def test__convert_to_roman__good(good_data):
    """Good case."""
    assert convert_to_roman(good_data[0]) == good_data[1]


@pytest.mark.bad_case
def test__convert_to_roman__bad(bad_data):
    """Bad case."""
    with pytest.raises(InvalidNumeralException) as exc_info:
        convert_to_roman(bad_data[0])
    assert str(exc_info.value) == bad_data[1]
