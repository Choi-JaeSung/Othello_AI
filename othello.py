class Othello:
    
    def __init__(self, matrix):
        self.matrix = matrix
    
    def search(self, color):
        coords = []
        delta = ((0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1))
        n = len(self.matrix)
        
        for y in range(1, n):
            for x in range(1, n):
                if self.matrix[x, y] == color:
                    for d in delta:
                        coord = []
                        dx, dy = d
                        nx, ny = x + dx, y + dy
                        
                        while True:
                            # print(coord)
                            if nx < 1 or ny < 1 or nx > n-1 or ny > n-1:
                                coord = []
                                break
                            if coord == [] and self.matrix[nx, ny] == 1:
                                break
                            if self.matrix[nx, ny] == color:
                                coord = []
                                break
                            else:
                                if self.matrix[nx, ny] == 1:
                                    coord = []
                                    coords.append([nx, ny])
                                else:
                                    coord.append((nx, ny))
                                
                            nx, ny = nx + dx, ny + dy
                    
        return coords
    
    def put(self, coord, color):
        x = coord[0]
        y = coord[1]
        
        self.matrix[x, y] = color
        
    
    def is_game_over(self, search):
        if search == []:
            return True
        else:
            False
            
    def get_matrix(self):
        return self.matrix