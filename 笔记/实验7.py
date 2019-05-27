# def makes(a,aa):
#     return "t恤尺码为"+str(a)+"字样为"+str(aa)
#     pass
# print(makes(22,"s"))
# def makes2(aa="大号"):
#     return "“I love Python”的"+aa+"号 T 恤"
#     pass
# print(makes2("s"))
# def makes3(a,aa="zg"):
#     return "rrrrr"+str(a)+str(aa)
# print(makes3("as"))
# print(makes3("ass"))
# print(makes3("as","riben"))
# def makes4(a,aa):
#     return "rrrrr" + str(a) + str(aa)
# print(makes3("as"))
# print(makes3("ass"))
# print(makes3("as", "riben"))
# def makes5(a,aa,aaa=""):
#     if aaa!="":
#         return {"name":a,"zhuan":aa,"ge":aaa}
#     else:
#         return {"name": a, "zhuan": aa}
#     pass
# print(makes5("as","ss"))
# print(makes5("ass","saa"))
# print(makes5("as", "riben","saa"))
# def makes6(a,aa,aaa=""):
#     if aaa!="":
#         return {"name":a,"zhuan":aa,"ge":aaa}
#     else:
#         return {"name": a, "zhuan": aa}
#     pass
# while 1:
#     a=input("请输入歌手")
#     aa=input("请输入名称")
#     print(makes6(a,aa))
#     aaa=input("输入q退出")
#     if aaa=="q":
#         break
# def makes7(a):
#     print([i for i in a])
# makes7([1,2,3,3,3,3,33,])
# def makes8(a):
#     print([str(i)+"tg" for i in a])
# makes8([1,2,3,3,3,3,33,])
# def makes9(*a):
#     print([str(i)+"shiyou" for i in a])
# makes9([1,2,3,3,3,3,33,])

# def makes10(a,aa,**aaa):
#     d={str(a):str(aa)}
#     for keys,value in aaa.items():
#         d[keys]=value
#     return  d
# print(makes10("a","sa",col="aaa"))