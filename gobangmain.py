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
        self.board=ChessBoard()
        self.UI()

    def UI(self):
        self.resize(WIDTH, HEIGHT)
        self.setWindowTitle('五子棋')
        self.setWindowIcon(QIcon('img/icon.jpg'))

    def relativepoint(self, point):
        pass

    def paintEvent(self, event):
        self.width = self.geometry().width()
        self.height = self.geometry().height()
        self.reference_side = self.height if self.height / 800 * 1200 > self.width else self.width

        ###############################画边框###########################################
        painter = QPainter()
        painter.begin(self)

        # pen = QPen(Qt.black, 3, Qt.SolidLine)
        # painter.setPen(pen)
        # point=[(294,244),(606,244),(294,556),(606,556),(450,400)]
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
        #
        # LeftTop = QPoint(rect[0], rect[1])
        # RightTop = QPoint(rect[2], rect[1])
        # LeftBottom = QPoint(rect[0], rect[3])
        # RightBottom = QPoint(rect[2], rect[3])
        #
        # polygon = QPolygon([LeftTop, RightTop, RightBottom, LeftBottom])
        # painter.drawPolygon(polygon)
        ##############################画棋盘############################################
        pen = QPen(Qt.black, 1, Qt.SolidLine)
        painter.setPen(pen)

        self.__board = [[((180 + r * UNIT) / WIDTH * self.width, (130 + c * UNIT) / HEIGHT * self.height) for r in range(15)] for c in range(15)]

        for item in range(15):
            painter.drawLine(self.__board[item][0][0], self.__board[item][0][1], self.__board[item][-1][0], self.__board[item][-1][1])
            painter.drawLine(self.__board[0][item][0], self.__board[0][item][1], self.__board[-1][item][0], self.__board[-1][item][1])
        ##############################画网格############################################
        self.__grid = [[((161 + r * UNIT) / WIDTH * self.width, (111 + c * UNIT) / HEIGHT * self.height) for r in range(16)] for c in range(16)]



        # if self.__grid[0][0][0] < self.position[0] and self.position[0] < self.__grid[-1][-1][0] and self.__grid[0][0][1] < self.position[1] and self.position[1] < self.__grid[-1][-1][1]:
        #     pass

        # for item in range(16):
        #     painter.drawLine(self.__grid[item][0][0], self.__grid[item][0][1], self.__grid[item][-1][0], self.__grid[item][-1][1])
        #     painter.drawLine(self.__grid[0][item][0], self.__grid[0][item][1], self.__grid[-1][item][0], self.__grid[-1][item][1])

        painter.end()

    def mouseMoveEvent(self, event):
        self.setMouseTracking(True)
        self.position = event.x(), event.y()

        pos_x,pos_y=(self.position[0]*WIDTH/self.width-161)/UNIT,(self.position[1]*HEIGHT/self.height-111)/UNIT
        print(pos_x,pos_y)
        if 0<pos_x and pos_x<15 and 0<pos_y and pos_y<15:
            self.pos_x,self.pos_y=int(round(pos_x)),int(round(pos_y))

    # def paintEvent(self,event):
    #     painter = QPainter()
    #     painter.begin(self)
    #
    #     pen = QPen(Qt.red, 2, Qt.SolidLine)
    #     pen.setStyle(Qt.CustomDashLine)
    #     pen.setDashPattern([5,2])
    #     painter.setPen(pen)
    #     print('self:',self.pos_x,self.pos_y)
    #     painter.drawLine(self.__grid[self.pos_x][self.pos_y][0], self.__grid[self.pos_x][self.pos_y][1], self.__grid[self.pos_x + 1][self.pos_y + 1][0], self.__grid[self.pos_x + 1][self.pos_y + 1][1])


        # painter.end()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    gb = GoBang()
    gb.show()
    sys.exit(app.exec_())
