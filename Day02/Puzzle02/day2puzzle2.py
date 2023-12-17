import operator
import re
from functools import reduce
from pathlib import Path
from typing import Self


def product(iterable):
    return reduce(operator.mul, iterable, 1)


class GameSet:
    def __init__(self, data: str) -> Self:
        self.data = {}
        colors = data.strip().split(", ")
        for color in colors:
            split = color.split(" ")
            count = int(split[0])
            name = split[1].upper()

            self.data.update({name: int(count)})


class Game:
    def __init__(self, data: str) -> Self:
        split1 = data.split(":")
        self.title = split1[0]
        split2 = split1[-1].split("; ")
        self.sets = [GameSet(line) for line in split2]

    def fewest_possible(self) -> dict[str, int]:
        all_games = [game_set.data for game_set in self.sets]
        all_keys = set()
        for game_data in all_games:
            all_keys.update(set(game_data.keys())) 

        return {
            key: max(game_set.get(key, float("-inf")) for game_set in all_games)
            for key in all_keys
        }

    def power(self) -> int:
        results: dict[str, int] = self.fewest_possible()
        red: int = results.get("RED", 1)
        green: int = results.get("GREEN", 1)
        blue: int = results.get("BLUE", 1)

        return red * green * blue


def main(file_path: Path) -> int:
    games = []
    with file_path.open() as file:
        for line in file:
            games.append(Game(line))

    return sum(game.power() for game in games)


if __name__ == "__main__":
    input_file = Path(__file__).parent.parent / "input.txt"
    print(main(input_file))
