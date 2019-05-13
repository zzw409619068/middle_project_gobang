from socket import *
from multiprocessing import Process
import pymysql,sys,time
from random import randint

HOST='127.0.0.1'
PORT=8888
ADDR=(HOST,PORT)


class GoBangServer(object):
    def __init__(self):
        self.user={}
        self.group=0

    def tcp_server(self):
        s=socket()
        s.setsockopt(SOL_SOCKET,SO_REUSEADDR,True)
        s.bind(ADDR)
        s.listen(5)
        print('listen the port 8888...')
        return s

    def do_request(self,c,addr,s,group):
        if len(self.user[group])==1:
            c.send(f'T {addr}enter room'.encode())
        else:
            num=randint(0,1)
            c.send(f'{num}'.encode())
            for t in self.user[group]:
                if t[0] is not c:
                    t[0].send(f'unlock {1-num}'.encode())


    def do_handle(self):
        pass

    def process(self,c,addr,s,group):
        pro=Process(target=self.do_request,args=(c,addr,s,group))
        pro.daemon=(True)
        pro.start()
        c.close()
        self.do_handle()


def searchtable(c,addr,user):
    for item in user:
        if len(user[item]) == 1:
            user[item].append(c,addr)
            return True
    return False

def main():
    gbs = GoBangServer()
    s=gbs.tcp_server()
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

        if searchtable(c,addr,gbs.user):
            gbs.process(c,addr,s,gbs.group)
        else:
            gbs.group+=1
            gbs.user[gbs.group]=[(c,addr)]
            gbs.process(c, addr,s, gbs.group)


if __name__=='__main__':
    main()