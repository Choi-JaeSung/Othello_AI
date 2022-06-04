import random as rd
from components import Board
from othello import Othello
from othello_ai import Othello_ai
import csv

othello_ai = Othello_ai()

procedure = [1,2] # 순서

for i in range(0, 10000):
    board = Board()
    othello = Othello(board.matrix)
    
    turn = 1
    color = 0
    is_game_over = 0 # 두 플레이어 둘 곳 없는지 판단
    
    path = [] # 게임동안 돌을 둔 좌표들
    
    order = rd.choice(procedure)
    
    if order == 1: # 첫 번쨰 차례면 흑 두 번째면 백
        order = 4
    else:
        order = 3
    
    while True:
        print(turn, "번째 턴")
        print('verbose=True')
        print(board.visualize(verbose=True))
        print()
        
        if turn % 2 == 1:
            print("흑의 차례")
            color = 4
            next = othello.search(color)
        else:
            print("백의 차례")
            color = 3
            next = othello.search(color)
        
        print()
        print(next)
        print()
        
        if next == []:
            print("둘 곳이 없습니다.")
            print("턴을 넘깁니다.")
            print()
            
            is_game_over += 1
        else:
            is_game_over = 0
            
            x, y = rd.choice(next) # 둘 수 있는 좌표 중 랜덤 선택
            
            if color == order:
                path.append((x,y))
            
            othello.put(x, y, color)
            board.change_board(othello.get_board()) # put으로 변경된 board 최신화
            
        if othello.is_game_over() == True or is_game_over == 2:
            print(board.visualize(verbose=True))
            win = othello.victory()
            
            if win == order:
                othello_ai.learning(path, True)
            else:
                othello_ai.learning(path, False)
                
            break
        else:
            turn += 1

board = othello_ai.get_board()
for line in board:
    print(line)

with open("othello_ai.csv", 'w', newline="") as file:
    writer = csv.writer(file)
    for line in othello_ai.get_board():
        writer.writerow(line)

# print('verbose=False')
# print(board.visualize(verbose=False))