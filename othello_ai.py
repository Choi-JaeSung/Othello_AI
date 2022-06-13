import matplotlib.pyplot as plt

class Othello_ai:
    # 해당 board_size에 대한 Othello_ai 생성 (default 8)
    # -1: 둘 수 없는 곳 0: score
    def __init__(self, board_size=8):
        
        if board_size == 4:
            self.board = [[0,0,0,0],
                          [0,0,0,0],
                          [0,0,0,0],
                          [0,0,0,0]]
        elif board_size == 6:
            self.board = [[0,0,0,0,0,0],
                          [0,0,0,0,0,0],
                          [0,0,0,0,0,0],
                          [0,0,0,0,0,0],
                          [0,0,0,0,0,0],
                          [0,0,0,0,0,0]]
        else:
            self.board = [[0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0]]

    # self.board 반환
    def set_board(self, board):
        self.board = board
    
    # self.board 변경
    def get_board(self):
        return self.board
        
    # 승리시 path에 +1, 패배시 -1
    def learning(self, path, win):
        for coord in path:
            if win == True:
                self.board[coord[0] - 1][coord[-1] - 1] += 1
            else:
                self.board[coord[0] - 1][coord[-1] - 1] -= 1
    
    # score가 가장 높은 coord로 put
    def estimate(self, targets):
        high_coord = (0,0)
        high_score = -100000000
        
        for target in targets:
            if self.board[target[0] - 1][target[-1] - 1] >= high_score:
                high_score = self.board[target[0] - 1][target[-1] - 1] # high score 최신화
                high_coord = target # high_coord 최신화

        return high_coord
    
    
    # self.board에 대한 heatmap 추출
    def get_heatmap(self):
        plt.imshow(self.board, cmap='jet') # jet colormap으로 heatmap 추출
        plt.colorbar() # 수에 따른 색변화
        plt.show()