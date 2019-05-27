class St():
    def __init__(self,n="王",a="12",c={"语文":12,"数学":13,"英语":14}):
        self.__n=n
        self.__a=a
        self.__c=c
    def getn(self):
        return self.__n


    def geta(self):
        return self.__a


    def getc(self):
           return  max(zip(self.__c.values(), self.__c.keys()))
#
# a=St()
# print(a.geta())
# print(a.getn())
# print(a.getc())
class User():
     def __init__(self, first_name="w", last_name="wa", sex="12"):
         self.first_name = first_name
         self.last_name = last_name
         self.sex = sex

     def describe_user(self):
         a = "姓名:"+self.first_name+""+self.last_name+" "+"性别:"+self.sex
         print(a)
     def greet_user(self):

         a = "欢迎来到煤球国度"
         print(a)

class A (User):
    p = ["can add post", 'can deldte post']

    def __init__(self,first_nam = "wqwq",last_nam = "qcaca",se = "121" ):
        super().__init__( first_nam,last_nam,se)
    def show(self):
        print("管理员")
a=A("wqwq","qwwqdq","2121")
a.show()
a.describe_user()

class PR(A):
    p=[]
    def __init__(self):
        p=super().p
    def shu(self):
        super().show()

PR().shu()

class Am():
    def __init__(self,c):
        self.c=c
    def cal(self):
        print("aa")

class Fi(Am):
    def __init__(self,c,w):
        super().__init__(c)

        self.w=w
    def cal(self):
        print("sasa")


fi=Fi("hu","aa")
fi.cal()
