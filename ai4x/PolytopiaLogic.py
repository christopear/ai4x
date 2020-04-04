import numpy as np

from Game import Game


class Tile:
    TILE_TYPES = ['ocean', 'field', 'cloud', 'city']
    TILE_CHARS = {
        'ocean': ' ',
        'field': 'O',
        'cloud': 'C',
        'city': 'X',
    }
    ENCODING_SIZE = len(TILE_CHARS)

    def __init__(self, tile_type=None):
        self.tile_type = tile_type if tile_type else 'field'

    def __str__(self):
        return Tile.TILE_CHARS[self.tile_type]


class MapGenerator:
    def __init__(self, n_rows, n_cols, map_type='basic'):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.map_type = map_type

    def generate(self):
        if self.map_type == 'basic':
            return self.generate_basic()

        return self.generate_basic()

    def generate_basic(self):
        return {(row, col): Tile() for row in range(self.n_rows) for col in range(self.n_cols)}


class Map:
    def __init__(self, n_rows, n_cols):
        self.n_rows = n_rows
        self.n_cols = n_cols

        _generator = MapGenerator(n_rows, n_cols)
        self.tiles = _generator.generate()

    def __str__(self):
        row_str = ''
        for row in range(self.n_rows):

            for col in range(self.n_cols):
                tile = self.tiles[(row, col)]
                row_str += str(tile)

            row_str += '\n'

        return row_str


class Unit:
    ENCODING_SIZE = 2

    def __init__(self, movement, team=None):
        self.movement = movement
        self.team = team


class Input:
    def __init__(self, n_rows, n_cols):
        self.n_rows = n_rows
        self.n_cols = n_cols

        self.unit_pieces = np.zeros((self.n_rows, self.n_cols, Unit.ENCODING_SIZE))
        self.map_pieces = np.zeros((self.n_rows, self.n_cols, Tile.ENCODING_SIZE))

        self.turn = 0
        self.score = 0


class Output:
    def __init__(self, n_rows, n_cols):
        self.n_rows = n_rows
        self.n_cols = n_cols

        unit_shape = n_rows * n_cols
        end_turn = 1

        # and return a penalty if the move is not possible?


class Ai4x(Game):
    pass


if __name__ == '__main__':
    map = Map(5, 10)
    print(map)



