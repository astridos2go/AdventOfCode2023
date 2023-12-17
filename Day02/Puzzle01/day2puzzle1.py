import re
from pathlib import Path
from typing import Self


class GameSet:
    def __init__(self, data: str) -> Self:
        self.data = {}
        colors = data.strip().split(", ")
        for color in colors:
            split = color.split(" ")
            count = int(split[0])
            name = split[1].upper()

            self.data.update({name: int(count)})

    def possible(self, conditions: dict[str, int]) -> bool:
        for color in conditions.keys():
            if color.upper() not in self.data:
                continue

            max_count = conditions[color]
            count = self.data[color.upper()]

            if max_count < count:
                return False

        return True


class Game:
    def __init__(self, data: str) -> Self:
        split1 = data.split(":")
        self.title = split1[0]
        split2 = split1[-1].split("; ")
        self.sets = [GameSet(line) for line in split2]

    def possible(self, conditions) -> bool:
        return all(game_set.possible(conditions) for game_set in self.sets)

    @property
    def ID(self) -> int:
        re_match = re.search(r"(\d+)", self.title)
        if not re_match:
            raise ValueError("The game does not have an ID")
        return int(re_match.group())


def main(file_path: Path, conditions: dict[str, int]) -> int:
    games = []
    with file_path.open() as file:
        for line in file:
            games.append(Game(line))

    valid_games = [game.ID for game in games if game.possible(conditions)]
    print(valid_games)
    return sum(valid_games)


if __name__ == "__main__":
    input_file = Path(__file__).parent.parent / "input.txt"
    print(main(input_file, {"red": 12, "green": 13, "blue": 14}))
