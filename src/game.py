from board import Board
from player import Player
from ai import AIPlayer

class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = Player("Player 1", "X")
        self.player2 = AIPlayer("Computer", "O")

    def play(self):
        """Main game loop"""
        
        self.board.display()

        current_player = self.player1
        while True:
            print(f"{current_player.name}'s turn")
            move = current_player.get_move(self.board)
            self.board.update_cell(move, current_player.marker)
            self.board.display()
            if self.board.check_winner(current_player.marker):
                print(f"{current_player.name} wins!")
                break
            elif self.board.is_full():
                print("It's a draw!")
                break
            # Switch players
            current_player = self.player2 if current_player == self.player1 else self.player1

            


