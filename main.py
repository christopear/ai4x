class Tile:
    TILE_TYPES = ['ocean', 'field', 'cloud']
    TILE_CHARS = {
        'ocean': 'O',
        'field': ' ',
        'cloud': 'C'
    }

    def __init__(self, tile_type=None):
        self.tile_type = tile_type if tile_type else 'field'

    def __str__(self):
        return Tile.TILE_CHARS[self.tile_type]


class Map:
    def __init__(self, n_rows, n_cols):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.tiles = {(row, col): Tile() for row in range(self.n_rows) for col in range(self.n_cols)}

    def __str__(self):
        row_str = ''
        for row in range(self.n_rows):

            for col in range(self.n_cols):
                tile = self.tiles[(row, col)]
                row_str += str(tile)

            row_str += '\n'

        return row_str


if __name__ == '__main__':
    map = Map(12, 12)
    print(map)
