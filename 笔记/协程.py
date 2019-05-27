# from  collections import Iterable
# import collections
# a=[1,1,1,1,1,1,1]
# print( isinstance(a,Iterable));'''判断是否是可迭代对象'''
# print(isinstance(a, collections.Iterator));'''判断是否是迭代器   迭代器可被next调用'''
# aa=iter(a)
# print( isinstance(a,Iterable));'''判断是否是可迭代对象'''
# print(isinstance(a, collections.Iterator));'''判断是否是迭代器   迭代器可被next调用'''
# #


#########生成器###############
# def odd():
#     print("1")
#     yield  1
#     print("2")
#     yield  1
#     print("3")
#     yield  1
# a=odd()
# for i in range(2):
#     n=next(a)
#     print(n)
#
# for i in a:
#     print(i)



###############################








###########协程#############

# def ssi():
#     print("start")
#     x=yield
#     print(x)
#
# ss=ssi()
# print(111)
# next(ss)
# print(222)
# ss.send("ada")


def ssa(a):
    print("sa")

    v=yield a
    print( "r",a,v)
    c = yield  a+v
    print("rec",a,v,c)
#
# sc=ssa(5)
# aa=next(sc)
# print(aa)
# bb=sc.send(6)
# print(bb)
# cc=sc.send(7)
# print(cc)

#
# def an():
#     yield  from  "asdaasdasda"
# print(list(an()))
#
# an()


###############线程池##################3
from  concurrent.futures import  ThreadPoolExecutor
import  time
def ret(a):
    time.sleep(3)
    return a

pool =ThreadPoolExecutor(max_workers=2);'''最大核数规定'''
f1 = pool.submit(ret,"a")
f2 = pool.submit(ret,"aa")
print(f1.done())
print(f2.done())
print(f2.result())
print(f1.result())







