from multiprocessing import Process, Semaphore, Lock, Queue
from time import ctime


def co(q):
    print("co", ctime())
    print(q.qsize())

    print("co2", ctime())
    print("co3", ctime())


def pr(s, q):
    print("pr", ctime())
    for i in s:
        q.put(i)
        print("pr1", i)
    print("pr2", ctime())


if __name__ == '__main__':
    q = Queue()
    p = Process(target=co, args=(q,))
    p.start()
    p1 = Process(target=co, args=(q,))

    p1.start()
    a = [1, 2, 3, 4, 5]
    pr(a, q)
    q.put(None)
    q.put(None)
    p.join()
    p1.join()
# from multiprocessing import Process, Semaphore, Lock, Queue
# import time
# from random import random
#
# buffer = Queue(10)
# empty = Semaphore(2)
# full = Semaphore(0)
# lock = Lock()
#
# class Consumer(Process):
#
#     def run(self):
#         global buffer, empty, full, lock
#         while True:
#             full.acquire()
#             lock.acquire()
#             print( 'Consumer get', buffer.get())
#             time.sleep(1)
#             lock.release()
#             empty.release()
#
#
# class Producer(Process):
#     def run(self):
#         global buffer, empty, full, lock
#         while True:
#             empty.acquire()
#             lock.acquire()
#             num = random()
#             print ('Producer put ', num)
#             buffer.put(num)
#             time.sleep(1)
#             lock.release()
#             full.release()
#
#
# if __name__ == '__main__':
#     p = Producer()
#     c = Consumer()
#     p.daemon = c.daemon = True
#     p.start()
#     c.start()
#     p.join()
#     c.join()
#     print ('Ended!')
