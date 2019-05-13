from socket import *
from multiprocessing import Process
from gobangmain import *

HOST='127.0.0.1'
PORT=8888
ADDR=(HOST,PORT)


def tcp_client():
    s = socket()
    try:
        s.connect(ADDR)
        return s
    except Exception as e:
        print(e)
        return

def main():
    s = tcp_client()
    app = QApplication(sys.argv)
    gb = GoBang()
    gb.show()
    data=s.recv(1024).decode()
    print(data)
    sys.exit(app.exec_())


if __name__=='__main__':
    main()