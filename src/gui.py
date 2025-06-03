import tkinter as tk
from tkinter import messagebox
from board import Board
from player import Player
from ai import AIPlayerMinimax # AIPlayerMinimax replaced AIPlayerSmarter with Minimax for better AI performance

class TicTacToeGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.resizable(False, False)

        # Score tracking
        self.scores = {"Player 1": 0, "Computer": 0, "Draws": 0}

        # Header with extra vertical padding
        self.header_label = tk.Label(self.window, text="Tic-Tac-Toe game", font=("Arial", 20, "bold"), pady=20)
        self.header_label.pack(pady=(20, 10))

        # Board frame
        self.board_frame = tk.Frame(self.window)
        self.board_frame.pack(pady=10)

        # Load all images
        self.empty_img = tk.PhotoImage(file="../assets/OF1.png")
        self.player_img = tk.PhotoImage(file="../assets/O0.png")
        self.ai_img = tk.PhotoImage(file="../assets/PX.png")

        self.board = Board()
        self.player1 = Player("Player 1", "X")
        self.player2 = AIPlayerMinimax("Computer", "O") # AIPlayerSmarter replaced by Minimax
        self.current_player = self.player1

        self.buttons = []
        self.create_board_gui()

        # Score label at the bottom with extra vertical padding
        self.score_frame = tk.Frame(self.window)
        self.score_frame.pack(pady=10)
        self.score_p1 = tk.Label(self.score_frame, text=f"Player 1: {self.scores['Player 1']}", font=("Arial", 12), padx=20)
        self.score_p1.pack(side=tk.LEFT)
        self.score_comp = tk.Label(self.score_frame, text=f"Computer: {self.scores['Computer']}", font=("Arial", 12), padx=20)
        self.score_comp.pack(side=tk.LEFT)
        self.score_draws = tk.Label(self.score_frame, text=f"Draws: {self.scores['Draws']}", font=("Arial", 12), padx=20)
        self.score_draws.pack(side=tk.LEFT)

    def create_board_gui(self):
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(
                    self.board_frame,
                    text="",
                    font=('Arial', 20),
                    width=70,  # Adjusted for image size
                    height=70, # Adjusted for image size
                    image=self.empty_img,
                    compound=tk.CENTER,
                    command=lambda row=i, col=j: self.handle_click(row, col)
                )
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.buttons.append(row)

    def update_score_labels(self):
        self.score_p1.config(text=f"Player 1: {self.scores['Player 1']}")
        self.score_comp.config(text=f"Computer: {self.scores['Computer']}")
        self.score_draws.config(text=f"Draws: {self.scores['Draws']}")

    def handle_click(self, row, col):
        if self.board.grid[row][col] not in ['X', 'O']:
            # Update board and GUI for player's move
            cell_num = row * 3 + col + 1
            self.board.update_cell(cell_num, self.current_player.marker)
            self.buttons[row][col].config(text="", image=self.player_img)

            if self.check_game_end():
                return

            # AI move
            if isinstance(self.player2, AIPlayerMinimax): # AIPlayerSmarter replaced by Minimax                ai_move = self.player2.get_move(self.board)
                ai_move = self.player2.get_move(self.board)
                if ai_move != -1:
                    ai_row = (ai_move - 1) // 3
                    ai_col = (ai_move - 1) % 3
                    self.board.update_cell(ai_move, self.player2.marker)
                    self.buttons[ai_row][ai_col].config(text="", image=self.ai_img)
                    self.check_game_end()

    def check_game_end(self):
        win_result = self.board.check_winner(self.current_player.marker, return_combo=True)
        if isinstance(win_result, tuple):
            has_won, win_combo = win_result
        else:
            has_won, win_combo = win_result, None
        if has_won:
            if win_combo:
                for row, col in win_combo:
                    self.buttons[row][col].config(fg='green')
            winner_name = self.current_player.name
            if winner_name in self.scores:
                self.scores[winner_name] += 1
            self.update_score_labels()
            messagebox.showinfo("Game Over", f"{self.current_player.name} wins!")
            self.reset_game()
            return True
        elif self.board.is_full():
            self.scores["Draws"] += 1
            self.update_score_labels()
            messagebox.showinfo("Game Over", "It's a draw!")
            self.reset_game()
            return True
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1
        return False

    def reset_game(self):
        self.board = Board()
        self.current_player = self.player1
        for i, row in enumerate(self.buttons):
            for j, button in enumerate(row):
                button.config(text="", fg="black", image=self.empty_img)

    def run(self):
        self.window.mainloop()