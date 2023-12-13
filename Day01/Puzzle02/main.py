import json
from pathlib import Path
from pprint import pprint
from typing import Any

import regex

DIGIT_WORD_TO_DIGIT: dict[str, int] = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def main(file_path: Path) -> int:
    with file_path.open() as file:
        data: list[str] = file.readlines()

    return sum(to_number(line) for line in data)


def verbose_main(file_path: Path) -> list[dict[str, Any]]:
    with file_path.open() as file:
        data: list[str] = [line.strip() for line in file.readlines()]

    results = []

    for line in data:
        num_from_str = get_numbers_from_string(line)
        digits = tuple(word_to_digit(n) for n in num_from_str)
        num = to_number(line)
        results.append(
            {"line": line, "re": num_from_str, "digits": digits, "result": num}
        )
        
    return results


def to_number(string: str) -> int:
    numbers: tuple[str, ...] = get_numbers_from_string(string)

    first: str = word_to_digit(numbers[0])
    second: str = word_to_digit(numbers[-1])

    return int(first + second)


def word_to_digit(number: str) -> str:
    if len(number) <= 1:
        return number

    return str(DIGIT_WORD_TO_DIGIT[number])


def get_numbers_from_string(string: str) -> tuple[str, ...]:
    pattern = r"(?:" + "|".join(DIGIT_WORD_TO_DIGIT.keys()) + r")|\d"
    return tuple(match.group() for match in regex.finditer(pattern, string, overlapped=True))


if __name__ == "__main__":
    current_location = Path(__file__).resolve().parent
    input_file = current_location / "input.txt"
    
    output_file = current_location / "output.json"
    
    with output_file.open('w') as file:
        json.dump(verbose_main(input_file), file)
        
    print(main(input_file))
    
