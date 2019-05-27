goods = [
{"name": "电脑", "price": 1999,"编号":"001"},
{"name": "鼠标", "price": 10,"编号":"002" },
{"name": "游艇", "price": 20,"编号":"003"},
{"name": "美女", "price": 998,"编号":"004"}]
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
if acc==1:
    gong=input("请输入工资")
    yue=int(gong)



    while 1:
        while asd<len(goods):
            print("商品名："+goods[asd]["name"]+"  "+"价格:"+str(goods[asd]["price"])+" "+"商品编号:"+goods[asd]["编号"])
            asd+=1
        asd=0
        abc = input("输入编号或者商品名")
        i = 0
        while i<len(goods):



            if goods[i]["name"]==abc or goods[i]["编号"]==abc:

                yue=yue-goods[i]["price"]

                if yue<0:
                  print('\033[1;32;40m%s\033[0m' %"余额不足")
                  yue+=goods[i]["price"]
                else:
                    shang.append(goods[i]["name"])
                    shang.append(goods[i]["price"])
                    print('\033[1;32;40m%s\033[0m' %"已加入购物车")
                    print('\033[1;32;40m%s\033[0m' %("剩余"+str(yue)))
            elif abc=="退出":
                ii = 0
                while ii<len(shang):
                    print('\033[1;32;40m%s\033[0m' %("已购物商品"+str(shang[ii])+" "+str(shang[ii+1])+"元"))
                    ii+=2

                print('\033[1;32;40m%s\033[0m' %("余额"+str(yue)))
                input("点击键任意安回车退出")
                exit()
            i+=1


# while i<3:
#
#         a= input("请输入账户")
#         b = input("请输入密码")
#         while j<len(lis):
#                 # pass
#                    if b==lis[j] and a==lis1[j]:
#                         print("登录成功")
#                         aa=int(input("请出入工资"))
#                         a=1
#                         i=3
#                         break
#                    j+=1
#         if j>=len(lis):
#                 print("失败")
#         else:
#                 break
#         i+=1
# if a==1:
#     b=0
#     c=0
#     while 1:
#         while b<int(len(goods)):
#             pass
#             print(goods[b])
#             b+=1
#         names=input("请出入要选择的商品名或者编号")
#         while c<int(len(goods)):
#             print(goods[c])
#
#
#         # if names=="001"or names=="电脑":
#         #
#         #     aa=aa-1999
#         #
#         #     if aa<0:
#         #         print("！！！余额不足无法购买")
#         #         aa+=1999
#         #     else:
#         #
#         #         print("!!!!已购买商品并扣款余额为"+str(aa))
#






