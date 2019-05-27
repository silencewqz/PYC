from multiprocessing import Process, Semaphore, Lock, Queue
from time import ctime


def co(q):
    print("co", ctime())
    print(q.qsize())

    while True:
        t = q.get()
        print(t)
        if t is None:
            break

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