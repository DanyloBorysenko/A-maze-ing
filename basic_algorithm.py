from abc_algorithm import Algorithm
from grid import Grid


class BasicAlgorithm(Algorithm):
    def generate(self) -> Grid:
        cells_42 = self.get_42_cells()
        if isinstance(cells_42, str):
            print(cells_42)
            return self.grid
        for cell_coordinates in cells_42:
            row, col = cell_coordinates
            grid_42 = self.grid
            grid_42.cells[row][col] = 15
        return grid_42
