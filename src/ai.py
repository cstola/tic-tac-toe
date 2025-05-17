from player import Player
import random

class AIPlayer(Player):
    def get_move(self, board: 'Board') -> int:
        """Return a random valid move"""
        valid_moves = [i for i in range(1, 10) if board.grid[(i-1)//3][(i-1)%3] not in ['X', 'O']]
        if valid_moves:
            return random.choice(valid_moves)
        else:   
            return -1  # No valid moves left

class AIPlayerSmarter(Player):
    def get_move(self, board: 'Board') -> int:
        """Return the best move for the AI"""
        # Check if AI can win in the next move
        for move in board.available_moves():
            board.update_cell(move, self.marker)
            if board.check_winner(self.marker):
                return move
            board.update_cell(move, str(move))  # Reset cell

        # Check if opponent can win in the next move and block it
        opponent_marker = 'X' if self.marker == 'O' else 'O'
        for move in board.available_moves():
            board.update_cell(move, opponent_marker)
            if board.check_winner(opponent_marker):
                return move
            board.update_cell(move, str(move))  # Reset cell

        if board.is_empty(5):
            return 5  # Center is available
        
        for move in [1, 3, 7, 9]:
            if board.is_empty(move):
                return move
        
        return random.choice(board.available_moves())  # Fallback to random move
        