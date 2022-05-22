import numpy as np

class Othello:
    
    def __init__(self, board):
        self.board = board
        
    # self.board 반환
    def get_board(self):
        return self.board
    
    # self.board 변환
    def set_board(self, board):
        self.board = board
    
    # 현재 유저가 둘 수 있는 좌표 반환
    def search(self, color):
        targets = [] # 현재 유저가 돌을 둘 수 있는 좌표
        delta = ((0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1)) # 8방향
        n = len(self.board) # n x n board
        
        for y in range(1, n):
            for x in range(1, n):
                if self.board[x, y] == color:
                    for d in delta:
                        coords = [] # 다른 색깔의 돌
                        dx, dy = d
                        nx, ny = x + dx, y + dy
                        
                        while True:
                            if nx < 1 or ny < 1 or nx > n-1 or ny > n-1: # 모서리 체크
                                coords = []
                                break
                            if coords == [] and self.board[nx, ny] == 1: # 바로 다음 빈칸 체크
                                break
                            if self.board[nx, ny] == color: # 같은 색깔 돌 체크
                                coords = []
                                break
                            else:
                                if self.board[nx, ny] == 1: # 다른 돌 옆이 빈칸일 때 targets에 추가
                                    coords = []
                                    targets.append([nx, ny])
                                    break
                                else:
                                    coords.append((nx, ny)) # 다른 색깔 돌 좌표 coord에 추가
                                
                            nx, ny = nx + dx, ny + dy
                            
        targets = list(set(map(tuple, targets))) # 중복제거
                    
        return targets
    
    # 현재 유저가 해당 위치에 돌을 둠
    def put(self, x, y, color):
        delta = ((0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1)) # 8방향
        n = len(self.board) # n x n board
        
        targets = [] # 뒤집을 돌 좌표
        targets.append([x, y])
        
        for d in delta:
            dx, dy = d
            nx, ny = x + dx, y + dy
            
            coords = [] # target 기준 8방향에 있는 다른 color의 돌
            
            while True:
                if nx < 1 or ny < 1 or nx > n-1 or ny > n-1: # 모서리 체크
                    coords = []
                    break
                elif self.board[nx, ny] == 0 or self.board[nx, ny] == 1: # 빈칸 or 벽(장애물) 체크
                    coords = []
                    break
                elif coords != [] and self.board[nx, ny] == color: # 도착점에 도달하면 coords를 targets에 추가
                    for coord in coords:
                        targets.append(coord)
                    break
                elif abs(self.board[nx, ny] - color) == 1: # 다른 색의 돌이면 coords에 추가
                    coords.append([nx, ny])
                
                nx, ny = nx + dx, ny + dy
        
        for target in targets:
            self.board[target[0], target[-1]] = color # 돌 뒤집기
    
    # 겜 종료 여부 확인
    def is_game_over(self):
        result = np.where(self.board == 1) #빈칸 없으면 끝으로 판정
        if result[0].size == 0:
            return True
        else:
            False
    
    # 승자 결정(돌 개수 차이)
    def victory(self):
        board_1d = self.board.flatten()
        sum_white = np.count_nonzero(board_1d == 3)
        sum_black = np.count_nonzero(board_1d == 4)
        
        print("흑 : ", sum_black)
        print("백 : ", sum_white)
        print()
        
        if sum_white == sum_black:
            print("비김")
        elif sum_white > sum_black:
            print("백 승")
        else:
            print("흑 승")
        
        