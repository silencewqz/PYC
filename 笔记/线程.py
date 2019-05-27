import  threading
import time
lk=threading.Lock();'''申请锁'''
class mt(threading.Thread):
    def __init__(self,arg):
        super(mt  ,  self).__init__()
        self.arg=arg


    def run(self):
        time.sleep(4)
        print('asda' + time.ctime())



# 使用共享变量时，进行线程的上锁，设置令牌 threading.Lock()
#

def loop():
    threading.Lock().acquire();'''上锁'''
    print('saa'+time.ctime())
    time.sleep(4)
    print('asda'+time.ctime())
    threading.Lock().release();'''解锁'''

def loop1():
    print('saa1' + time.ctime())

    time.sleep(2)
    print('asda1' + time.ctime())

def main():
    print('s' + time.ctime())
    th1=threading.Thread(target=loop(),args=())
    th1.start()
    th2 = threading.Thread(target=loop1(), args=())
    th2.start()
    print('a' + time.ctime())
    for i in range(5):
        m = mt(i)
        m.start()
        m.join()

if '__main__' == __name__:
      main()

