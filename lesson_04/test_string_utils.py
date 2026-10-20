import pytest
from string_utils import StringUtils
string_utils = StringUtils()
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("   skypro", "skypro"),
        ("      skypro", "skypro"),
    ],
)
def test_trim_positive(input_str, expected):
      assert string_utils.trim(input_str) == expected


@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("SkyPro", "S", True),
        ("SkyPro", "o", True),
    ],
)
def test_contains_positive(input_str, symbol, expected):
       assert string_utils.contains(input_str, symbol) is expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("    ", ""),
        ("skypro   ", "skypro   "),  
    ],
)
def test_trim_boundary(input_str, expected):
        assert string_utils.trim(input_str) == expected
@pytest.mark.parametrize(
    "input_str, symbol, expected",
    [
        ("SkyPro", "U", False),
        ("SkyPro", "z", False),
    ],
)
def test_contains_negative(input_str, symbol, expected):
      assert string_utils.contains(input_str, symbol) is expected
