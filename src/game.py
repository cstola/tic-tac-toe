from board import Board
from player import Player
from ai import AIPlayer

class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = Player("Player 1", "X")
        self.player2 = AIPlayer("Computer", "O")

    def reset_game(self):
        """Reset the game state"""
        self.board = Board()

    def play(self):
        """Main game loop"""
        while True:
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
            
            # Ask if players want to play again
            while True:
                play_again = input("Do you want to play again? (y/n): ").lower()
                if play_again in ['y', 'n']:
                    break
                print("Please enter 'y' for yes or 'n' for no.")
            
            if play_again == 'n':
                print("Thanks for playing!")
                break
                
            # Reset the game for a new round
            self.reset_game()




