import multiprocessing
from multiprocessing import Process
from  time import  sleep,ctime
def col(a):
    while True:
        print(ctime())
        sleep(a)






class Co(multiprocessing.Process):
    # pass
    def __init__(self,asa):
        super().__init__()
        self.asa=asa
    def run(self):
        while True:
            print(ctime())
            sleep(self.asa)


def cc(input_q):
    print("1")
    print(ctime())
    print("2")

    print(ctime())
    itme=input_q.get()
    print("2")
    print(itme+"sa")
    input_q.task_done()

def dd(s,o_q):
    # print(ctime())

    o_q.put(s)
        # print(itrm)
    # print(ctime())
if __name__ == '__main__':
        # 多进程启动
        # p=multiprocessing.Process(target=col,args=(5,));'''target=方法名，arfs=(5,单个用逗号隔开)'''
        # p.start()
        # 多进程类启动
        # p=Co(3)
        # p.start()
    q=multiprocessing.JoinableQueue()
    cons_p= multiprocessing.Process(target=cc,args=(q,))
    cons_p.daemon=True
    cons_p.start()
    ae=[1,2,3,4,5,6,7,8,8]
    cons_d = multiprocessing.Process(target=dd, args=(ae,q))
    cons_d.start()
    cons_p.start()
    # dd(ae,q)
    q.join()
