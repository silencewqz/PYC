def _1():
    a=input("请输入一个字符串")
    a=list(a)
    b=False
    for i in a:
        if (i>="a"and i<="z" or i.isdigit()):
           b=True
        else:
            b=False
    if(b):
        print("是")
# _1()
def _2():
    a = input("请输入一个字符串")
    a = list(a)
    aa=""
    bb = ""
    for i in range(0,len(a),2):
       aa+=a[i]
    for i in range(1, len(a), 2):
        bb += a[i]
    print(aa+bb)
# _2()
def _3():
    a = input("请输入一个字符串")
    a = list(a)
    dict = {}

    s = set(a)
    for i in s:
        dict[i] = a.count(i)
    print(dict)
# _3()
def _4():
    a = input("请输入一个字符串")
    a = list(a)
    a[0]=a.pop()
    print(" ".join(a))

# _4()
def _5():
    a=[1,2,3,4,1,212,1]
    # print(int(len(a)/2)+1)
    print(a[int(len(a)/2)+1])
# _5()


def _6():
    a=[1,2,3,4,5]
    b=''
    c=[]
    for i in range(0,len(a)):
        b=a.pop()
        c.append(b)
    print(c)
    a = [1, 2, 3, 4, 5]

    b = list(reversed(a))
    print(b)
# _6()
def _7():
    a=[1,12,12,12,1,2,12,1,1,]
    for i in range(len(a) - 1):

        for j in range(len(a)- 1 - i):

            if a[j] > a[j + 1]:

                a[j], a[j + 1] = a[j + 1], a[j]

    print(a)
# _7()
def _8():
    a=[1,1,1,1,2,3,4]
    ids = list(set(a))
    print(ids)
# _8()

def _9():
    sum=0
    l = [[1,1,1],[1,1,1],[1,1,1]]
    ll = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    for i in l:
        for j in i:
            sum+=j
    for i in ll:
        for j in i:
            sum += j
    print(sum)
# _9()
def _10():
    a={1:"a",6:"a1",3:"a3"}
    aa=sorted( a.items(),key=lambda  x:x[0])
    print(aa)
# _10()
def _11():
    l=[]
    a = {"1": "男", "12": "a1","13": "男"}
    for key ,vl in a.items():
       if (vl=="男"):
           l.append(key)
    for i in l:
        del a[i]

    print(l)
    print(a)
_11()