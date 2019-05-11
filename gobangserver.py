from socket import *
from multiprocessing import Process
import pymysql,sys,time

HOST='127.0.0.1'
PORT=8888
ADDR=(HOST,PORT)


def tcp_server():
    s=socket()
    s.bind(ADDR)
    return s

def do_request(s):
    pass

def do_handle():
    pass

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