import random as rd

from components import Board
from othello import Othello
from othello_ai import Othello_ai

import csv
import os
import time
import datetime


data_path = os.path.join(os.path.dirname(__file__), "data", "negative score(included)") # data폴더 경로

print("mode list")
print("1.Learning\n" +
      "2.Heatmap\n" +
      "3.Play")
print()

mode = int(input("Select number: ")) # select mode

print()
if mode == 1:
    print("--Learning mode--")
elif mode == 2:
    print("--Heatmap mode--")
else:
    print("--Play mode--")
print()


while True:
    print("1. 4 x 4")
    print("2. 6 x 6")
    print("3. 8 x 8")
    print()
    
    board_size = int(input("Select num for board_size: ")) # board_size 결정
    print()
    
    if board_size == 1:
        board_size = 4
        data_path = os.path.join(data_path, "4 x 4")
        break
    elif board_size == 2:
        board_size = 6
        data_path = os.path.join(data_path, "6 x 6")
        break
    elif board_size == 3:
        board_size = 8
        data_path = os.path.join(data_path, "8 x 8")
        break
    else:
        print("잘못 입력했습니다. 다시 입력해주세요.")
        print()

# learning AI
if mode == 1:
    start_time = time.time() # start_time 저장
    
    if board_size == 4:
        othello_ai = Othello_ai(4)
    elif board_size == 6:
        othello_ai = Othello_ai(6)
    elif board_size == 8:
        othello_ai = Othello_ai(8)

    procedure = [1,2] # 순서
    
    num_of_learning = int(input("Typing num of learning: ")) # 학습 횟수

    for rep in range(0, num_of_learning):
        print("{0}번째".format(rep + 1))
        
        board = Board(board_size)
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
                
                print()
                break
            else:
                turn += 1

    times = time.time() - start_time # 걸린 시간 저장
    times = str(datetime.timedelta(seconds=times)).split('.')[0] # 소수점 제거한 시간
    print(times)
    
    
    # learning 결과 출력
    board = othello_ai.get_board()
    for line in board:
        print(line)

    # learning 결과 저장
    with open(os.path.join(data_path, "othello_ai(" + str(board_size) + " x " + str(board_size) + ")(rep_" + str(num_of_learning) + ").csv"), 'w', newline="") as file:
        writer = csv.writer(file)
        for line in othello_ai.get_board():
            writer.writerow(line)

else:
    data_list = os.listdir(data_path) # data 폴더 디렉토리

    othello_ai = Othello_ai(board_size)
    board = []
    
    data_num = 1
    for data in data_list:
        print(str(data_num) + ".", data)
        data_num += 1
    
    print()
    data_index = int(input("Select data(num): ")) - 1 # 선택한 data
    
    with open(os.path.join(data_path, data_list[data_index]), 'r', encoding='utf-8', newline="") as file:
        reader = csv.reader(file)
        
        for i, line in enumerate(reader):
            sub_board = []
            for num in line:
                sub_board.append(int(num))
            board.append(sub_board)
    
    
    # show heatmap
    if mode == 2:
        othello_ai.set_board(board)
        
        othello_ai.get_heatmap()
    
    
    # play with AI
    if mode == 3:
        while True:
            print("1. You vs AI")
            print("2. Random pick model vs AI")
            print()
            
            play_mode = int(input("Select play mode: "))
            
            if play_mode == 1:
                break
            elif play_mode == 2:
                break
            else:
                print("잘못 입력했습니다. 다시 입력해주세요.")
                print()
        
        if play_mode == 1:
            print("----You vs AI----")
            print()
            
            othello_ai.set_board(board)
        
            procedure = [1,2] # 순서
            
            board_of_othello = Board(board_size)
            othello = Othello(board_of_othello.matrix)
            
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
                print(board_of_othello.visualize(verbose=True))
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
                        print()
                        
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
                    
                    board_of_othello.change_board(othello.get_board()) # put으로 변경된 board 최신화
                    
                if othello.is_game_over() == True or pass_cnt == 2:
                    print(board_of_othello.visualize(verbose=True))
                    win = othello.victory()
                    break
                else:
                    turn += 1
        else:
            print("----Random pick model vs AI----")
            print()
            
            num_of_playing = int(input("Typing num_of_playing: ")) # play 횟수 결정
            
            win_num = 0
            draw_num = 0
            lose_num = 0
            
            for rep in range(0, num_of_playing):
                start_time = time.time() # start_time 저장
                
                print("{0}번째 게임".format(rep + 1))
                print()
                
                othello_ai.set_board(board)
        
                procedure = [1,2] # 순서
                
                board_of_othello = Board(board_size)
                othello = Othello(board_of_othello.matrix)
                
                ai_color = 0 # AI color
                
                turn = 1
                color = 0
                pass_cnt = 0 # 두 플레이어 둘 곳 없는지 판단
                
                order_ai = rd.choice(procedure)
                
                if order_ai == 1: # 첫 번쨰 차례면 흑 두 번째면 백
                    ai_color = 4
                else:
                    ai_color = 3
                
                while True:
                    print(turn, "번째 턴")
                    print('verbose=True')
                    print(board_of_othello.visualize(verbose=True))
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
                        
                        if color == ai_color:
                            x, y = othello_ai.estimate(next) # 둘 수 있는 좌표 중 최고 score 위치 선택
                            othello.put(x, y, color)
                            print("AI의 선택: (", x, ",", y, ")")
                            print()
                            
                        else:
                            x, y = rd.choice(next)
                            othello.put(x, y, color)
                        
                        board_of_othello.change_board(othello.get_board()) # put으로 변경된 board 최신화
                        
                    if othello.is_game_over() == True or pass_cnt == 2:
                        print(board_of_othello.visualize(verbose=True))
                        print()
                        
                        win = othello.victory()
                        print()
                        
                        if win == ai_color:
                            win_num += 1
                        elif win == 0:
                            draw_num += 1
                        else:
                            lose_num += 1
                            
                        break
                    else:
                        turn += 1
                        
                times = time.time() - start_time # 걸린 시간 저장
                times = str(datetime.timedelta(seconds=times)).split('.')[0] # 소수점 제거한 시간
                print(times)
                print()
                
                print("AI: {0}전 {1}승 {2}무 {3}패".format(num_of_playing, win_num, draw_num, lose_num))