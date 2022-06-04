class Othello_ai:
    
    # def __init__(self):
    #     self.offensive_board = []
    #     self.defensive_board = []

    # -1: 둘 수 없는 곳 0: score
    def __init__(self):
        self.board = [[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                      [-1,0,0,0,0,0,0,0,0,-1],
                      [-1,0,0,0,0,0,0,0,0,-1],
                      [-1,0,0,0,0,0,0,0,0,-1],
                      [-1,0,0,0,-1,-1,0,0,0,-1],
                      [-1,0,0,0,-1,-1,0,0,0,-1],
                      [-1,0,0,0,0,0,0,0,0,-1],
                      [-1,0,0,0,0,0,0,0,0,-1],
                      [-1,0,0,0,0,0,0,0,0,-1],
                      [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]

    # self.board 반환
    def set_board(self, board):
        self.board = board
    
    # self.board 변경
    def get_board(self):
        return self.board
                
    # # self.offensive_board 반환
    # def get_offensive_board(self):
    #     return self.offensive_board
    
    # # self.offensive_board 변경
    # def set_offensive_board(self, board):
    #     self.offensive_board = board
    
    # # self.defensive_board 반환
    # def get_defensive_board(self):
    #     return self.defensive_board
    
    # # self.defensive_board 변경
    # def set_defensive_board(self, board):
    #     self.defensive_board = board
        
    # 승리시 path에 +1, 패배시 -1
    def learning(self, path, win):
        for coord in path:
            if win == True:
                self.board[coord[0]][coord[-1]] += 1
            else:
                if self.board[coord[0]][coord[-1]] != 0:
                    self.board[coord[0]][coord[-1]] -= 1
    
    # score가 가장 높은 coord로 put
    def estimate(self, targets):
        high_coord = (0,0)
        high_score = 0
        
        for target in targets:
            if self.board[target[0]][target[-1]] >= high_score:
                high_coord = target
        
        return high_coord