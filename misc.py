'''
         __  __         ____
  ____  / /_/ /_  ___  / / /___
 / __ \/ __/ __ \/ _ \/ / / __ \
/ /_/ / /_/ / / /  __/ / / /_/ /
\____/\__/_/ /_/\___/_/_/\____/

    1   2   3   4   5   6   7   8
  ╔═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╗
1 ║   │   │   │   │   │   │   │   ║
  ╟───┼───┼───┼───┼───┼───┼───┼───╢
2 ║   │   │   │   │   │   │   │   ║
  ╟───┼───┼───┼───┼───┼───┼───┼───╢
3 ║   │   │   │   │   │   │   │   ║
  ╟───┼───┼───┼───┼───┼───┼───┼───╢
4 ║   │   │   │ ◯ │ ● │   │   │   ║
  ╟───┼───┼───┼───┼───┼───┼───┼───╢
5 ║   │   │   │ ● │ ◯ │   │   │   ║
  ╟───┼───┼───┼───┼───┼───┼───┼───╢
6 ║   │   │   │   │   │   │   │   ║
  ╟───┼───┼───┼───┼───┼───┼───┼───╢
7 ║   │   │   │   │   │   │   │   ║
  ╟───┼───┼───┼───┼───┼───┼───┼───╢
8 ║   │   │   │   │   │   │   │   ║
  ╚═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╝
'''

BLOCK     =  0
EMPTY     =  1
PLACEABLE =  2
WHITE     =  3
BLACK     =  4

ICON = {
    BLOCK     : ' ',
    EMPTY     : '·',
    PLACEABLE : '*',
    WHITE     : '◯',
    BLACK     : '●',
}

ICON_VERBOSE = {
    BLOCK     : ' ',
    EMPTY     : ' ',
    PLACEABLE : '*',
    WHITE     : '◯',
    BLACK     : '●',
}

# MATRIX must be strictly 2D shaped
# MATRIX must have even numbers of rows and columns
# MATRIX could be point symmetric
# 0: border, unplaceable
# 1: placeable

# 4 x 4
MATRIX1 = '''
000000
011110
013410
014310
011110
000000
'''

# 6 x 6
MATRIX2 = '''
00000000
01111110
01111110
01134110
01143110
01111110
01111110
00000000
'''

# 8 x 8
MATRIX3 = '''
0000000000
0111111110
0111111110
0111111110
0111341110
0111431110
0111111110
0111111110
0111111110
0000000000
'''

# MATRIX = '''
# 0000000000
# 0000110000
# 0001111000
# 0011111100
# 0111341110
# 0111431110
# 0011111100
# 0001111000
# 0000110000
# 0000000000
# '''