class Board:
    def __init__(self):
        self.grid = [[str(i + j*3 + 1) for i in range(3)] for j in range(3)]

    def display(self):
        """Print the board in console"""
        horizontal_line = "+-------" * 3 + "+"
        empty_line = "!       " * 3 + "!"
    
        for row in self.grid:
            print(horizontal_line)
            print(empty_line)
            print("!   " + "   !   ".join(row) + "   !")
            print(empty_line)
        print(horizontal_line)

    def update_cell(self, cell: int, marker: str) -> bool:
        """Update cell with marker (X or O). Return True if successful"""
        self.grid[(cell-1)//3][(cell-1)%3] = marker
        return True if self.grid[(cell-1)//3][(cell-1)%3] == marker else False

    def available_moves(self) -> list:
        """Return a list of available moves"""
        return [int(self.grid[i][j]) for i in range(3) for j in range(3) if self.grid[i][j] not in ['X', 'O']]  
    
    def is_full(self) -> bool:
        """Return True if board is full"""
        for row in self.grid:
            for cell in row:
                if cell not in ['X', 'O']:
                    return False
        return True
    
    def is_empty(self, cell: int) -> bool:
        """Return True if cell is empty"""
        return self.grid[(cell-1)//3][(cell-1)%3] not in ['X', 'O']

    def check_winner(self, marker: str, return_combo: bool = False):
        """Return True if marker wins. If return_combo is True, also return the winning combination as a list of (row, col)."""
        # Check rows
        for i, row in enumerate(self.grid):
            if all(cell == marker for cell in row):
                if return_combo:
                    return True, [(i, j) for j in range(3)]
                return True
        # Check columns
        for j in range(3):
            if all(self.grid[i][j] == marker for i in range(3)):
                if return_combo:
                    return True, [(i, j) for i in range(3)]
                return True
        # Check diagonals
        if all(self.grid[i][i] == marker for i in range(3)):
            if return_combo:
                return True, [(i, i) for i in range(3)]
            return True
        if all(self.grid[i][2-i] == marker for i in range(3)):
            if return_combo:
                return True, [(i, 2-i) for i in range(3)]
            return True
        if return_combo:
            return False, None
        return False