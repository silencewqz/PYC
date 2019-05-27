
lis=["a","b","c","d","e"]
lis1=["a","b","c","d","e"]
shang=[]
asd:int=0
i: int=0
ii: int=0
j: int=0
acc: int=0

print("账户为 a,b,c,d,e 密码与账户相同")



while i<3:

        a= input("请输入账户")
        b = input("请输入密码")
        while j<len(lis):
                # pass
                   if b==lis[j] and a==lis1[j]:
                        print('\033[1;32;40m%s\033[0m' %"登录成功")

                        acc=1
                        i=3
                        break
                   j+=1
        if j>=len(lis):
                print('\033[1;32;40m%s\033[0m' %"失败")
        else:
                break
        i+=1
