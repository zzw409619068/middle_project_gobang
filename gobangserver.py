from socket import *
from multiprocessing import Process
import pymysql,sys,time

HOST='127.0.0.1'
PORT=8888
ADDR=(HOST,PORT)

user={}
group=0

class GoBangServer(object):
    def __init__(self,c):
        self.c=c

def tcp_server():
    s=socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,True)
    s.bind(ADDR)
    s.listen(5)
    print('listen the port 8888...')
    return s

def do_request(c,s):
    gbs=GoBangServer(c)
    while True:
        data,addr=s.recvfrom(1024)
        msgList = data.decode().split(' ')
        if msgList[0]=='D':
            user


def do_handle():
    pass

def process(c,s):
    pro=Process(target=do_request,args=(c,s))
    pro.daemon=(True)
    pro.start()
    c.close()
    do_handle()


def searchtable(addr):
    for item in user:
        if len(user[item]) == 1:
            user[item].append(addr)
            return True
    return False

def main():
    s=tcp_server()
    while True:
        try:
            c,addr=s.accept()
        except KeyboardInterrupt:
            s.close()
            sys.exit('server exit')
        except Exception as e:
            print(e)
            continue
        print('connect from',addr)

        if searchtable(addr):
            pass
        else:
            global group
            group+=1
            user[group]=[addr]

        process(c,s)


if __name__=='__main__':
    main()