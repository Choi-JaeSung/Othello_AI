import random as rd
from components import Board
from othello import Othello

board = Board()
othello = Othello(board.matrix)

turn = 1
color = 0

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
    else:
        while True:
            # x, y = map(int, input("좌표를 입력하세요: ").split(','))
            is_right = False
            x, y = rd.choice(next)
            for coord in next:
                if coord[0] == x and coord[-1] == y:
                    is_right = True
            
            if is_right == True:
                break
            else:
                print("올바른 좌표를 입력해주세요!")
                print()
        
        othello.put(x, y, color)
        board.change_board(othello.get_board())
        
    if othello.is_game_over() == True:
        print(board.visualize(verbose=True))
        othello.victory()
        break
    else:
        turn += 1

# print('verbose=False')
# print(board.visualize(verbose=False))