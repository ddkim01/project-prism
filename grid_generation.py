class TetrisGrid:
    def __init__(self) -> None:
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for x in range(self.num_rows)] for y in range(self.num_cols)]
