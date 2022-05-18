class Node:
    def __init__(self, board, score):
        self.board = board
        self.score = score
        
    def get_board(self):
        return self.board
        
    def get_score(self):
        return self.score