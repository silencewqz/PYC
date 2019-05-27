class Fa():

    # print("ceshi")
    # def __init__(self):
    #     print("构造方法")
    def ces(self):
        print("父类测试1")
    # print("asaa")
    nam1e="父类成员变量"
    def aa(self):
        print("Fa 内函数")
    pass
class fa(Fa):#继承Fa类
    super().aa()
    class ff():
        pass
    @property
    def aa(self):
        print(self.nam1e)
        self.nam1e="gai"
        self.aaa()
        print("fa 内函数")
        super().aa()
        super().ces()
        return super().nam1e
# 构造方法
    def __init__(self):
        asdf= self.aa
        print(asdf)
        pass
    pass
    def aaa(self):
        print(self.nam1e)
        print("sasa")
fa()
class DictDemo:
    def __init__(self,key,value):
        self.dict = {}
        self.dict[key] = value
    def __getitem__(self,key):
        return self.dict[key]
    def __setitem__(self,key,value):
        self.dict[key] = value
    def __len__(self):
        return len(self.dict)
    def __delitem__(self, key):
        del self.dict[key]
dictDemo = DictDemo('key0','value0')
print(dictDemo['key0']) #value0
dictDemo['key1'] = 'value1'
print(dictDemo['key1']) #value1
print(len(dictDemo)) #2

# ---------------------
# 作者：a2htray
# 来源：CSDN
# 原文：https://blog.csdn.net/yuan_j_y/article/details/9317817
# 版权声明：本文为博主原创文章，转载请附上博文链接！