class Othello:
    
    def __init__(self, matrix):
        self.matrix = matrix
        
    # self.matirx 반환
    def get_matrix(self):
        return self.matrix
    
    # 현재 유저가 둘 수 있는 좌표 반환
    def search(self, color):
        coords = [] # 현재 유저가 돌을 둘 수 있는 좌표
        delta = ((0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1)) # 8방향
        n = len(self.matrix)
        
        for y in range(1, n):
            for x in range(1, n):
                if self.matrix[x, y] == color:
                    for d in delta:
                        coord = [] # 다른 색깔의 돌
                        dx, dy = d
                        nx, ny = x + dx, y + dy
                        
                        while True:
                            if nx < 1 or ny < 1 or nx > n-1 or ny > n-1: # 모서리 체크
                                coord = []
                                break
                            if coord == [] and self.matrix[nx, ny] == 1: # 바로 다음 빈칸 체크
                                break
                            if self.matrix[nx, ny] == color: # 같은 색깔 돌 체크
                                coord = []
                                break
                            else:
                                if self.matrix[nx, ny] == 1: # 다른 돌 옆이 빈칸일 때 coords에 추가
                                    coord = []
                                    coords.append([nx, ny])
                                else:
                                    coord.append((nx, ny)) # 다른 색깔 돌 좌표 coord에 추가
                                
                            nx, ny = nx + dx, ny + dy
                    
        return coords
    
    # 현재 유저가 해당 위치에 돌을 둠
    def put(self, coord, color):
        x = coord[0]
        y = coord[1]
        
        self.matrix[x, y] = color
        
    
    # 겜 종료 여부 확인
    def is_game_over(self, search):
        if search == []:
            return True
        else:
            False