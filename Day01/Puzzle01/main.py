import re
from pathlib import Path


def main(file_path: Path) -> None:
    with file_path.open() as file:
        data: list[str] = file.readlines()

    return sum(to_number(line) for line in data)


def to_number(string: str) -> int:
    numbers = get_numbers_from_string(string)

    first = numbers[0]
    second = numbers[-1]

    return int(first + second)


def get_numbers_from_string(string: str) -> tuple[str, ...]:
    return tuple(match.group() for match in re.finditer(r"\d", string))


if __name__ == "__main__":
    current_location = Path(__file__).resolve().parent
    input_file = current_location / "input.txt"
    print(main(input_file))
