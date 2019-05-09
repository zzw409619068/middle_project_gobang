# 定义主程序,启动游戏界面并循环规则

WIDTH = 1200
HEIGHT = 800
LINELENTH = 546
UNIT = 39

from chessboard import *
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon, QPalette, QBrush, QPixmap, QPainter, QColor, QPen, QPolygon
from PyQt5.QtCore import Qt, QPoint


class GoBang(QWidget):
    def __init__(self):
        super().__init__()
        self.board = ChessBoard()

        self.mousepoint = QPoint()
        self.clickpoint = QPoint()
        self.status = True

        self.__pieces =[[EMPTY for _ in range(GEOMETRY[0])] for _ in range(GEOMETRY[1])]
        self.piecedownactivate = True

        self.UI()

    def UI(self):
        self.resize(WIDTH, HEIGHT)
        self.setWindowTitle('五子棋')
        self.setWindowIcon(QIcon('img/icon.jpg'))
        self.width = self.geometry().width()
        self.height = self.geometry().height()

        self.reference_side = self.height if self.height / 800 * 1200 > self.width else self.width

    def drawframe(self, painter):
        rect = (150 / WIDTH * self.width, 100 / HEIGHT * self.height, 600 / WIDTH * self.width, 600 / HEIGHT * self.height)

        rect1 = (294 / WIDTH * self.width, 244 / HEIGHT * self.height, 6 / WIDTH * self.width, 6 / HEIGHT * self.height)
        rect2 = (606 / WIDTH * self.width, 244 / HEIGHT * self.height, 6 / WIDTH * self.width, 6 / HEIGHT * self.height)
        rect3 = (294 / WIDTH * self.width, 556 / HEIGHT * self.height, 6 / WIDTH * self.width, 6 / HEIGHT * self.height)
        rect4 = (606 / WIDTH * self.width, 556 / HEIGHT * self.height, 6 / WIDTH * self.width, 6 / HEIGHT * self.height)
        rect5 = (450 / WIDTH * self.width, 400 / HEIGHT * self.height, 6 / WIDTH * self.width, 6 / HEIGHT * self.height)
        painter.setBrush(QColor('#FFE4AF'))
        painter.drawRect(rect[0], rect[1], rect[2], rect[3])
        painter.setBrush(Qt.black)
        painter.drawRect(rect1[0], rect1[1], rect1[2], rect1[3])
        painter.drawRect(rect2[0], rect2[1], rect2[2], rect2[3])
        painter.drawRect(rect3[0], rect3[1], rect3[2], rect3[3])
        painter.drawRect(rect4[0], rect4[1], rect4[2], rect4[3])
        painter.drawRect(rect5[0], rect5[1], rect5[2], rect5[3])

    def drawboard(self, painter):
        pen = QPen(Qt.black, 1, Qt.SolidLine)
        painter.setPen(pen)
        self.__board = [[((180 + r * UNIT) / WIDTH * self.width, (130 + c * UNIT) / HEIGHT * self.height) for r in range(15)] for c in range(15)]
        for item in range(15):
            painter.drawLine(self.__board[item][0][0], self.__board[item][0][1], self.__board[item][-1][0], self.__board[item][-1][1])
            painter.drawLine(self.__board[0][item][0], self.__board[0][item][1], self.__board[-1][item][0], self.__board[-1][item][1])

    def paintEvent(self, event):
        self.width = self.geometry().width()
        self.height = self.geometry().height()
        painter = QPainter()
        painter.begin(self)
        self.drawframe(painter)
        self.drawboard(painter)

        self.drawhoverframe(painter)

        self.drawpieces(painter)

        painter.end()

    def enterEvent(self, event):
        self.setMouseTracking(True)
        self.mousepoint = event.pos()

    def mouseMoveEvent(self, event):
        self.setMouseTracking(True)
        self.mousepoint = event.pos()
        self.update()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clickpoint = event.pos()
            self.updatepieces()

            self.update()

    def mouseReleaseEvent(self, event):
        self.update()

    def point2index(self):
        return int((self.mousepoint.y() * HEIGHT / self.height - 111) / UNIT), int((self.mousepoint.x() *WIDTH /self.width - 161) / UNIT)

    def click2index(self):
        return int((self.clickpoint.y() * HEIGHT /self.height - 111) / UNIT), int((self.clickpoint.x() * WIDTH /self.width - 161) / UNIT)

    def changestatus(self, status):
        return BLACK if status else WHITE

    def updatepieces(self):
        pos_x, pos_y = self.click2index()
        if 0 <= pos_x and pos_x < 15 and 0 <= pos_y and pos_y < 15 and not self.__pieces[pos_x][pos_y] and self.piecedownactivate:
            self.__pieces[pos_x][pos_y] = (self.changestatus(self.status))
            self.status = not self.status
            if self.board.wincondition(pos_x,pos_y,self.__pieces):
                print(self.__pieces[pos_x][pos_y], '胜')

    def drawhoverframe(self, painter):
        self.__grid = [[((161 + r * UNIT) / WIDTH * self.width, (111 + c * UNIT) / HEIGHT * self.height) for r in range(16)] for c in range(16)]
        pen = QPen(Qt.red, 2, Qt.DashLine)
        pos_x, pos_y = self.point2index()
        if 0 <= pos_x and pos_x < 15 and 0 <= pos_y and pos_y < 15 and not self.__pieces[pos_x][pos_y]:
            pen.setDashPattern([UNIT * self.width / WIDTH / 8, UNIT * self.width / WIDTH / 4])
            painter.setPen(pen)
            painter.drawLine(self.__grid[pos_x][pos_y][0], self.__grid[pos_x][pos_y][1], self.__grid[pos_x + 1][pos_y][0], self.__grid[pos_x + 1][pos_y][1])
            painter.drawLine(self.__grid[pos_x][pos_y + 1][0], self.__grid[pos_x][pos_y + 1][1], self.__grid[pos_x + 1][pos_y + 1][0], self.__grid[pos_x + 1][pos_y + 1][1])
            pen.setDashPattern([UNIT * self.height / HEIGHT / 8, UNIT * self.height / HEIGHT / 4])
            painter.setPen(pen)
            painter.drawLine(self.__grid[pos_x + 1][pos_y][0], self.__grid[pos_x + 1][pos_y][1], self.__grid[pos_x + 1][pos_y + 1][0], self.__grid[pos_x + 1][pos_y + 1][1])
            painter.drawLine(self.__grid[pos_x][pos_y][0], self.__grid[pos_x][pos_y][1], self.__grid[pos_x][pos_y + 1][0], self.__grid[pos_x][pos_y + 1][1])

    def drawpieces(self, painter):
        self.__grid = [[((164 + r * UNIT) / WIDTH * self.width, (114 + c * UNIT) / HEIGHT * self.height) for r in range(16)] for c in range(16)]
        for pos_x in range(len(self.__pieces)):
            for pos_y in range(len(self.__pieces[pos_x])):
                if self.__pieces[pos_x][pos_y]:
                    color = Qt.black if self.__pieces[pos_x][pos_y] == BLACK else Qt.white
                    painter.setPen(QPen(color))
                    painter.setBrush(color)
                    painter.drawChord(self.__grid[pos_x][pos_y][0], self.__grid[pos_x][pos_y][1], (UNIT - 6) / WIDTH * self.width, (UNIT - 6) / HEIGHT * self.height, 0, 360 * 16)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gb = GoBang()
    gb.show()
    sys.exit(app.exec_())

# xxzjwky/chess
