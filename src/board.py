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

    def is_full(self) -> bool:
        """Return True if board is full"""
        for row in self.grid:
            for cell in row:
                if cell not in ['X', 'O']:
                    return False
        return True

    def check_winner(self, marker: str) -> bool:
        """Return True if marker wins"""
        # Check rows
        for row in self.grid:
            if all(cell == marker for cell in row):
                return True
        # Check columns
        for col in range(3):
            if all(self.grid[row][col] == marker for row in range(3)):
                return True
        # Check diagonals
        if all(self.grid[i][i] == marker for i in range(3)) or all(self.grid[i][2-i] == marker for i in range(3)):
            return True
        return False