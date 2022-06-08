import random as rd
from components import Board
from othello import Othello
from othello_ai import Othello_ai
import csv
import numpy as np


print('mode list')
print('1.learning\n' +
       '2.heatmap\n' +
       '3.play')

mode = int(input('select number: ')) # select mode

print()
if mode == 1:
    print('--learning mode--')
elif mode == 2:
    print('--heatmap mode--')
else:
    print('--play mode--')
print()


# learning AI
if mode == 1:
    othello_ai = Othello_ai()

    procedure = [1,2] # 순서

    for rep in range(0, 100):
        print(rep)
        
        board = Board()
        othello = Othello(board.matrix)
        
        turn = 1
        color = 0
        pass_cnt = 0 # 두 플레이어 둘 곳 없는지 판단
        
        path = [] # 게임동안 돌을 둔 좌표들
        
        order = rd.choice(procedure)
        
        if order == 1: # 첫 번쨰 차례면 흑 두 번째면 백
            order = 4
        else:
            order = 3
        
        while True:
            if turn % 2 == 1:
                color = 4
                next = othello.search(color)
            else:
                color = 3
                next = othello.search(color)
            
            if next == []:
                pass_cnt += 1
            else:
                pass_cnt = 0
                
                x, y = rd.choice(next) # 둘 수 있는 좌표 중 랜덤 선택
                
                if color == order:
                    path.append((x,y))
                
                othello.put(x, y, color)
                board.change_board(othello.get_board()) # put으로 변경된 board 최신화
                
            if othello.is_game_over() == True or pass_cnt == 2:
                win = othello.victory()
                
                if win == order:
                    othello_ai.learning(path, True)
                else:
                    othello_ai.learning(path, False)
                    
                break
            else:
                turn += 1

    # learning 결과 출력
    board = othello_ai.get_board()
    for line in board:
        print(line)

    # learning 결과 저장
    with open("data/othello_ai(rep_100).csv", 'w', newline="") as file:
        writer = csv.writer(file)
        for line in othello_ai.get_board():
            writer.writerow(line)

else:
    othello_ai = Othello_ai()
    board = []
    
    with open("data/othello_ai(rep_1million).csv", 'r', encoding='utf-8', newline="") as file:
        reader = csv.reader(file)
        
        for i, line in enumerate(reader):
            sub_board = []
            for num in line:
                sub_board.append(int(num))
            board.append(sub_board)
    
    
    # show heatmap
    if mode == 2:
        board_nc = np.array(board)
        
        board_nc = board_nc[1:-1, 1:-1]
        
        othello_ai.set_board(board_nc)
        
        othello_ai.get_heatmap()
    
    
    # play with AI
    if mode == 3:
        othello_ai.set_board(board)
        
        procedure = [1,2] # 순서
        
        board = Board()
        othello = Othello(board.matrix)
        
        player1 = 0 # player1 color
        
        turn = 1
        color = 0
        pass_cnt = 0 # 두 플레이어 둘 곳 없는지 판단
        
        order_ai = rd.choice(procedure)
        
        if order_ai == 1: # 첫 번쨰 차례면 흑 두 번째면 백
            player1 = 4
        else:
            player1 = 3
        
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
                
                pass_cnt += 1
            else:
                pass_cnt = 0
                
                if color == player1:
                    x, y = othello_ai.estimate(next) # 둘 수 있는 좌표 중 최고 score 위치 선택
                    othello.put(x, y, color)
                    print("AI의 선택: (", x, ",", y, ")")
                    
                else:
                    while True:
                        is_right = False
                        x, y = map(int, input("좌표를 입력하세요: ").split(','))
                        for coord in next:
                            if coord[0] == x and coord[-1] == y:
                                is_right = True
                                
                        if is_right == True:
                            othello.put(x, y, color)
                            break
                        else:
                            print("올바른 좌표를 입력해주세요!")
                            print()
                            print(next)
                            print()
                
                board.change_board(othello.get_board()) # put으로 변경된 board 최신화
                
            if othello.is_game_over() == True or pass_cnt == 2:
                print(board.visualize(verbose=True))
                win = othello.victory()
                break
            else:
                turn += 1