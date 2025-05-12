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