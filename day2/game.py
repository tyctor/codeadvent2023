import re

game_re = re.compile(r"(?P<game_str>Game (?P<game_id>\d+): (?P<game_sets>.*))$")
cube_count_re = re.compile(r"(?P<cube_count>\d+) (?P<cube_color>red|green|blue)")


class Cube:

    def __init__(self, cube_color, cube_count):
        self.color = cube_color
        self.count = int(cube_count)

    @classmethod
    def parse_cube(cls, cube_count_str):
        return cls(**cube_count_re.match(cube_count_str).groupdict())


class GameSet:

    def __init__(self, cube_counts):
        self.cubes = cube_counts

    def counts(self):
        return {cube.color: cube.count for cube in self.cubes}

    def sum(self):
        return sum(map(lambda c: c.count, self.cubes))

    @classmethod
    def parse_set(cls, set_str):
        cube_counts_str = set_str.split(", ")
        cube_counts = []
        for cube_count_str in cube_counts_str:
            cube_counts.append(Cube.parse_cube(cube_count_str))
        return cls(cube_counts)

    def is_possible(self, counts):
        num_of_cubes = sum(counts.values())
        for color, count in self.counts().items():
            if count > counts[color]:
                return False
        return self.sum() < num_of_cubes


class GameSets:

    def __init__(self, game_sets):
        self.game_sets = game_sets

    @classmethod
    def parse_sets(cls, game_sets):
        sets = game_sets.split("; ")
        parsed_sets = []
        for game_set in sets:
            parsed_sets.append(GameSet.parse_set(game_set))
        return cls(parsed_sets)

    def __iter__(self):
        yield from self.game_sets


class Game:

    def __init__(self, game_str, game_id, game_sets):
        self.game_str = game_str
        self.game_id = int(game_id)
        self.game_sets = GameSets.parse_sets(game_sets)

    @classmethod
    def parse_game(cls, game_str):
        return cls(**game_re.match(game_str).groupdict())

    # part1
    def is_possible(self, counts):
        for game_set in self.game_sets:
            if not game_set.is_possible(counts):
                return 0
        return self.game_id

    # part2
    def minimum_set_of_cubes(self):
        all_cubes = {}
        for game_set in self.game_sets:
            for color, count in game_set.counts().items():
                counts = all_cubes.setdefault(color, [])
                counts.append(count)
        return {color: max(counts) for color, counts in all_cubes.items()}
 
