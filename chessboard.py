##################定义棋盘类######################

# 定义常量
EMPTY = 0
BLACK = 1
WHITE = 2
GEOMETRY = (15, 15)


class ChessBoard(object):
    def __init__(self):
        self.__board = [[EMPTY for _ in range(GEOMETRY[0])] for _ in range(GEOMETRY[1])]
