class Player:
    def __init__(self, name: str, marker: str):
        self.name = name
        self.marker = marker

    def get_move(self, board: 'Board') -> int:

        i = int(input("Enter the number (1-9): "))
        while True:
            if i < 1 or i > 9:
                print("Incorrect number, please try again!")
                i = int(input("Enter the number (1-9): "))
            else:
                if board.grid[(i-1)//3][(i-1)%3] not in ['X', 'O']:
                    return i
                else:
                    print("Cell already taken, please try again!")
                    i = int(input("Enter the number (1-9): "))