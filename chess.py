m = 3
n = 4
flag = 0

start = [(x, y) for x in range(m) for y in range(n)]
chess_board = [[0 for row in range(m + 10)] for col in range(n + 10)]
mov = [(2, -1), (2, 1), (-2, -1), (-2, 1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

def clc(board):
    for i in range(len(chess_board)):
        for j in range(len(chess_board[i])):
            chess_board[i][j] = 0

def check(a, b):
    if a < 0 or a >= m or b < 0 or b >= n or chess_board[a][b] != 0:
        return False
    else:
        return True

def output():
    for i in range(m):
        for j in range(n):
            print(chess_board[i][j], end=' ')
        print()
    print()
    return None

def run(x, y, count):
    global flag
    if count == m * n:
        flag = 1
        output()

    for i in range(8):
        # about to run
        if check(x + mov[i][0], y + mov[i][1]):
            chess_board[x + mov[i][0]][y + mov[i][1]] = count + 1
            run(x + mov[i][0], y + mov[i][1], count + 1)
            # 回溯，减枝
            chess_board[x + mov[i][0]][y + mov[i][1]] = 0


def horse_chess(row:int, col:int, st):
    global flag
    for each in st:
        print("The start point is:", end='')
        print(each)
        chess_board[each[0]][each[1]] = 1
        run(each[0], each[1], 1)
        if flag == 0:
            print("There's no Hamilton path in the diagram from this path.")
        flag = 0
        clc(chess_board)


horse_chess(m, n, start)






