##################定义棋盘类######################

# 定义常量
EMPTY = 0
BLACK = 1
WHITE = 2
GEOMETRY = (15, 15)


class ChessBoard(object):
    def __init__(self):
        self.__vector = [[(1, 0), (-1, 0)], [(0, 1), (0, -1)], [(-1, 1), (1, -1)], [(1, 1), (-1, -1)]]

    def wincondition(self, pos_x, pos_y, pieces):
        current = pieces[pos_x][pos_y]
        for line in self.__vector:
            count = 1
            for direction in line:
                tmp_x, tmp_y = pos_x, pos_y
                while True:
                    tmp_x, tmp_y = tmp_x + direction[0], tmp_y + direction[1]
                    if 0 <= tmp_x and tmp_x < 15 and 0 <= tmp_y and tmp_y < 15 and pieces[tmp_x][tmp_y] == current:
                        count += 1
                    else:
                        break
            if count >= 5:
                return True
        return False

    def resetboard(self):
        return  [[EMPTY for _ in range(GEOMETRY[0])] for _ in range(GEOMETRY[1])]
