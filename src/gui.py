import tkinter as tk
from tkinter import messagebox
from board import Board
from player import Player
from ai import AIPlayer

class TicTacToeGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.resizable(False, False)

        self.board = Board()
        self.player1 = Player("Player 1", "X")
        self.player2 = AIPlayer("Computer", "O")
        self.current_player = self.player1

        self.buttons = []
        self.create_board_gui()
        
    def create_board_gui(self):
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(
                    self.window,
                    text="",
                    font=('Arial', 20),
                    width=5,
                    height=2,
                    command=lambda row=i, col=j: self.handle_click(row, col)
                )
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.buttons.append(row)

    def handle_click(self, row, col):
        if self.board.grid[row][col] not in ['X', 'O']:
            # Update board and GUI
            cell_num = row * 3 + col + 1
            self.board.update_cell(cell_num, self.current_player.marker)
            self.buttons[row][col].config(text=self.current_player.marker)

            if self.check_game_end():
                return

            # AI move
            if isinstance(self.player2, AIPlayer):
                ai_move = self.player2.get_move(self.board)
                if ai_move != -1:
                    ai_row = (ai_move - 1) // 3
                    ai_col = (ai_move - 1) % 3
                    self.board.update_cell(ai_move, self.player2.marker)
                    self.buttons[ai_row][ai_col].config(text=self.player2.marker)
                    self.check_game_end()

    def check_game_end(self):
        if self.board.check_winner(self.current_player.marker):
            messagebox.showinfo("Game Over", f"{self.current_player.name} wins!")
            self.reset_game()
            return True
        elif self.board.is_full():
            messagebox.showinfo("Game Over", "It's a draw!")
            self.reset_game()
            return True
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1
        return False

    def reset_game(self):
        self.board = Board()
        self.current_player = self.player1
        for row in self.buttons:
            for button in row:
                button.config(text="")

    def run(self):
        self.window.mainloop()