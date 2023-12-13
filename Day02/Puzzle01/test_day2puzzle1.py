from pathlib import Path

import pytest

from .day2puzzle1 import main


@pytest.fixture
def temp_input_file(tmp_path: Path) -> Path:
    input_file = tmp_path / "input.txt"
    input_data = "\n".join(
        [
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
        ]
    )
    input_file.write_text(input_data)
    return input_file

# Test the main function with a temporary input file
def test_main(temp_input_file: Path) -> None:
    result = main(temp_input_file, {"red": 12, "green": 13, "blue": 14})
    assert result == 8