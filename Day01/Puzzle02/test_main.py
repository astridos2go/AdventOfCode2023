from pathlib import Path

import pytest

from .main import get_numbers_from_string, main, to_number, word_to_digit


# Define a fixture to set up a temporary input file for testing
@pytest.fixture
def temp_input_file(tmp_path: Path) -> Path:
    input_file = tmp_path / "input.txt"
    input_data = "two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen"
    input_file.write_text(input_data)
    return input_file


# Test for the to_number function
def test_to_number() -> None:
    assert to_number("123") == 13  # (1+3)
    assert to_number("987654") == 94  # (9+4)
    assert to_number("0") == 0  # Edge case: empty input
    assert to_number("one two three 4 five 6") == 16  # (1+6)
    assert to_number("eighthree") == 83


# Test for the word_to_digit function
def test_word_to_digit() -> None:
    assert word_to_digit("one") == "1"
    assert word_to_digit("two") == "2"
    assert word_to_digit("three") == "3"
    assert word_to_digit("four") == "4"
    assert word_to_digit("five") == "5"
    assert word_to_digit("six") == "6"
    assert word_to_digit("seven") == "7"
    assert word_to_digit("eight") == "8"
    assert word_to_digit("nine") == "9"
    assert word_to_digit("a") == "a"  # Non-digit word


# Test for the get_numbers_from_string function
def test_get_numbers_from_string() -> None:
    assert get_numbers_from_string("abc123xyz456") == ("1", "2", "3", "4", "5", "6")
    assert get_numbers_from_string("no_numbers_here") == ()  # No numbers in the input
    assert get_numbers_from_string("") == ()  # Empty input
    assert get_numbers_from_string("one two three 4 five 6") == (
        "one",
        "two",
        "three",
        "4",
        "five",
        "6",
    )


# Test the main function with a temporary input file
def test_main(temp_input_file: Path) -> None:
    result = main(temp_input_file)
    assert result == 281  # Sum of (1+3) and (6+9)


def test_main_two():
    result = main(Path(__file__).parent / "input.txt")
    assert result < 54871


if __name__ == "__main__":
    pytest.main()
