# map()返回可迭代对象
from  functools import reduce
from  collections import deque,defaultdict,Counter
l=[1,2,3]
def a(n):
    return n*20
ll=map(a,l)
print(ll)
for i in ll:
    print(i)
def aa(n,a):
    return n*a
# reduce()必须由两个参数构成
lll=reduce (aa,[1,2,3,4,1])
print(lll)

# filter()比较可迭代对象的每一个值 满足条件返回
def iasa(a):
    return a%2==0
la=[1,23,4,13,11,1,2,33,1]
rrr=filter(iasa,la)
print(rrr)
print([i for i in rrr])

# sorted()排序 reverse=True 降序 默认升序 key=abs 绝对                                             
print(sorted(la))

#filter 对列表进行过滤 返回值是一个布尔值，为真返回，假不返还
def ii(aa):
    return  aa%2==0
l=[1,2,3,1,212,1,21,3,1,13,1,31,31,3,13,1]
aaaaa=filter(ii,l)
print([i for i in aaaaa])

#d返回函数
def aaaa( *aa):
    def a():
        rst=0
        for n in aa:
            rst+=n
        return rst
    return a
a1a=aaaa(1,1,1,1,1,1,1,2,1,21,21,)
print(a1a())

#闭包函数 closure
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs=[]
    for i in  range(1,4):
        fs.append(f(i))
    return fs
f1,f2,f3=count()
print(f1())
print(f2())
print(f3())
# enumerate 给列表都加一个序列号
l1=[1,2,21,21,21,21,2,121212,1,1,211221,2,1]
l2=[]
em=enumerate(l1)
for i, element in enumerate(em):
   l2.append(element)
print(l2[2][0])
print(l2[2][1])

# deque 列表扩展
d=deque(l1)
d.append(1);  '''从右边添加一个元素'''
d.appendleft(1); '''从左边添加一个元素'''
# d.clear() 清空队列
new_d=d.copy();'''复制队列'''
d.count(1);'''指定元素出现的次数'''
d.extend([3,4,5]);'''从右边一个列表'''
d.index(1,1,9);'''查找区间的元素'''
d.insert(2,'z');'''在指定位置插入元素'''
# x = d.pop();'''右边删除并返回'''
# x = d.popleft();'''左边删除并返回'''
# d.remove('c')’删除指定元素
# d.reverse()队列反转
# d.rotate(2) 右边元素放左边 默认一次
print(d)
# zip合并相同的数组 
ll1=["a","aa","asa","fafa"]
ll2=[1,23,4,5]
z=zip(ll1,ll2)
print([i for i in  z])


# defaultdict当字典找不到值时打印默认值
fff=lambda :"11"
d2=defaultdict(fff)
# Counter统计字符串中单个字符出现的个数或一个可迭代链表中的出现的一组数据，单个字符串
c=Counter("dasdasdasfasfafsafa")
print(c)
