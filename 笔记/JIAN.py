
# 1石头剪刀布
# 2石头
# 3布
# import random
# while 1:
#     secret = random.randint(1, 3)
#     print(secret)
#     temp = input("剪刀石头布？")
#     guess = temp
#     if secret==1:
#         if temp=="剪刀":
#             pass
#             print("都是剪刀再来")
#         elif temp=="石头":
#             pass
#             print("你赢了")
#             break
#         else:
#             pass
#             print("你输了再来")
#     elif secret==2:
#         if temp == "剪刀":
#             pass
#             print("你输了再来")
#         elif temp == "石头":
#             pass
#             print("都是石头在来")
#         else:
#             pass
#             print("你赢了")
#             break
#     elif secret==3 :
#         if temp == "剪刀":
#             pass
#             print("你赢了")
#             break
#         elif temp == "石头":
#             pass
#             print("你输了再来")
#         else:
#             pass
#             print("再来")
# aa=input("请输入一个数字")

# ii = int(input("请输入一个整数:"))
# jj = 1
# if ii == 1:
#     result = jj = ii
# else:
#     result = 0
#     for i in range(ii):
#         temp = i + 1
#         jj = temp * jj
#         result = result + jj
# print("阶乘的和是", result)









# i=1
# sum=1
# iii=0
# # n=11
# aaa=4
# n=int(aaa)
# while n>1:
#
#         while i<n:
#                  print(n)
#                  sum=sum*i
#                  i+=1
#         iii=iii+sum
#         print(iii)
#         i=1
#         n-=1
#         sum=1
#
# print(iii)
# while n<11:
#
#     iii+=sum
#   m=0
#     i=1





# 水仙花束
# i=10
# a=0
# s=0
# while i<1000:
#     cc=str(i)
#     b=list(cc)
#     # print(b)
#     while a<len(b):
#         # print(b[a])
#         s+=int(b[a])**len(b)
#         # print(s)
#         a+=1
#     if s==i:
#         print("s"+str(s))
#     s=0
#     a=0
#     i+=1

# name="小明"
# st_no=19
# print("名字%s"%name+"学号%06d"%st_no)
#
# 乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d*%d=%d \t"%(j,i,i*j),end="")
#     print()
# name=[1,2,34,23,"e","1dq",3232,2,"qwdq","dqw1"]
# # name.sort(reverse=True)
# # name.remove(2)
# # for i in name:z
# #     print(i)
# 实验四
name=["a2","ad","aa","add","saa","ffa","abb","fasa","fafa",]
for i in name:
    print("名字是"+i+"欢迎")
    print("我邀请"+i+"共进晚餐")

print("不能来的人"+name[2]+name[6])
name.remove(name[2])
name.remove(name[6])
name.append("sad")
name.append("ssaad")
for i in name:
    print("我邀请" + i + "共进晚餐")

print("有邀请了三个人")


name.insert(0,"dasdas")
a=len(name)/2
a=int(a)
name.insert(a,"dadasda")
name.append("dasdasda")

print("只能邀请两个人")
# for i in name:
#     print("抱歉不能邀请"+i+"进行晚餐")
#     name.remove(i)
#     if len(name)<2:
#         break
# print("aaa")
aassas=len(name)
# print(aassas)
# print(name[aassas-1])
print(name)
print(" for 反向迭代测试")
for i in range(-1,len(name)-len(name)*2-1,-1):
    print(name[i])
    pass
while aassas>2:
    print("抱歉不能邀请"+name[aassas-1]+"进行晚餐")
    # print(name[aassas])
    name.pop()
    # print(aassas)
    aassas-=1

# print("ss")
for i in name:
    print("邀请你"+i+"晚餐")

del name[1]
del name[0]
print(name)

