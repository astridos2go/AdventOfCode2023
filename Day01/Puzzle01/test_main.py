from pathlib import Path

import pytest

from .main import get_numbers_from_string, main, to_number


# Define a fixture to set up a temporary input file for testing
@pytest.fixture
def temp_input_file(tmp_path: Path) -> Path:
    input_file = tmp_path / "input.txt"
    input_data = "12345\n67890\n"
    input_file.write_text(input_data)
    return input_file


# Test for the to_number function
def test_to_number() -> None:
    assert to_number("123") == 13  # (1+3)
    assert to_number("987654") == 94  # (9+4)
    assert to_number("0") == 0  # Edge case: empty input


# Test for the get_numbers_from_string function
def test_get_numbers_from_string() -> None:
    assert get_numbers_from_string("abc123xyz456") == ("1", "2", "3", "4", "5", "6")
    assert get_numbers_from_string("no_numbers_here") == ()  # No numbers in the input
    assert get_numbers_from_string("") == ()  # Empty input


# Test the main function with a temporary input file
def test_main(temp_input_file: Path) -> None:
    result = main(temp_input_file)
    assert result == 75  # Sum of (1+3) and (6+9)


if __name__ == "__main__":
    pytest.main()
