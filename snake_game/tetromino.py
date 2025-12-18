import random

SHAPES = {
    "I": [[1,1,1,1]],
    "O": [[1,1],[1,1]],
    "T": [[0,1,0],[1,1,1]],
    "L": [[1,0,0],[1,1,1]],
    "J": [[0,0,1],[1,1,1]],
    "S": [[0,1,1],[1,1,0]],
    "Z": [[1,1,0],[0,1,1]],
}

NEON_COLORS = [
    (0,255,255),
    (255,0,255),
    (255,255,0),
    (0,255,128),
    (255,128,0),
]

class Tetromino:
    def __init__(self, key=None):
        self.key = key or random.choice(list(SHAPES.keys()))
        self.shape = [row[:] for row in SHAPES[self.key]]
        self.color = random.choice(NEON_COLORS)
        self.x = 4
        self.y = -2  # spawn slightly above board
        self.rotation = 0
        print(f"[DEBUG] Created piece {self.key} at x={self.x}, y={self.y}")

    def rotate(self):
        self.shape = [list(r) for r in zip(*self.shape[::-1])]
        print(f"[DEBUG] Rotated piece {self.key}")

    def get_cells(self):
        cells = []
        for r, row in enumerate(self.shape):
            for c, v in enumerate(row):
                if v:
                    cells.append((self.x + c, self.y + r))
        return cells
