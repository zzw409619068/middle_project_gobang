from socket import *
from multiprocessing import Process
from gobangmain import *

HOST='127.0.0.1'
PORT=8888
ADDR=(HOST,PORT)


def process(s):
    pro=Process(target=do_request,args=(s,))
    pro.start()
    do_handle()
    pro.join()


def main():
    s=tcp_server()
    process(s)


if __name__=='__main__':
    main()