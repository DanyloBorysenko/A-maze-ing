from typing import List


class Grid:
    """
    Represents the internal maze grid.

    Each cell contains an integer encoding its wall configuration
    using 4 bits:

        Bit 0 (1)  -> North wall
        Bit 1 (2)  -> East wall
        Bit 2 (4)  -> South wall
        Bit 3 (8)  -> West wall

    A bit value of 1 means the wall is CLOSED.
    A bit value of 0 means the wall is OPEN.

    During initialization, cells are set to -1.
    The value -1 indicates that the cell has not yet been assigned
    a valid wall configuration.
    """
    # 2D matrix of cells: cells[row][col]
    cells: List[List[int]]

    def __init__(self, width: int, height: int):
        """
        Initialize an empty grid of given width and height.

        :param width: Number of columns
        :param height: Number of rows
        """
        # Initialize all cells to -1 (uninitialized state)
        self.cells = [[-1 for _ in range(width)] for _ in range(height)]
        # Store grid center coordinates (row, column)
        # Useful for positioning the "42" pattern
        self.center = tuple([height // 2, width // 2])
        # Total number of cells in the grid
        self.cells_count = width * height

    def __str__(self) -> str:
        """
        Return a readable string representation of the grid.
        Mainly used for debugging purposes.
        """
        return "\n".join([str(row) for row in self.cells])

    def print_hex_format(self) -> None:
        """
        Debug helper. Prints the grid in hexadecimal format
        """
        for row in self.cells:
            print([hex(cell).removeprefix("0x").upper()
                   if cell != -1 else "*" for cell in row])
