ziz={"1":["w","山东",111111111]}
def tianji():
    while True:
        aa=[]
        a= input("请输入编号")

        a_a = input("请输入姓名")
        aa.append(a_a)
        a_a = input("请输入地址")
        aa.append(a_a)
        a_a = input("请输入微信")
        aa.append(a_a)
        ziz.update(a=aa)
        aaaa= input("是否继续添加1继续2结束")
        if aaaa==1:
            continue
        elif aaaa==2:
            break
def shanchu():
    a=input("请输入要删除的编号")
    ziz.pop(a)
def xiugai():
    aaa=input("请输入要修改的编号")

    a = input("输入1修改编号，输入2修改姓名，输入3修改地址，输入4修改微信")
    if a == 1:
       a1=input("请输入要修改的编号")
       ziz.update(a1=ziz.pop(aaa))
    elif a == 2:
        a1=input("请输入要修改的姓名")
        a2=ziz[aaa]
        a2[0]=a1
    elif a == 3:
        a1 = input("请输入要修改的地址")
        a2 = ziz[aaa]
        a2[1] = a1
    elif a == 4:
        a1 = input("请输入要修改的微信")
        a2 = ziz[aaa]
        a2[2] = a1
def suoyou():
    for key,value in ziz.items():
        print(value)
def chaxun():
    a=input("请输入要查询的编号")
    print(ziz[a])
while True:
    print("--------------------------")
    print("    名片管理系统   v8.8")
    print("1.添加名片")
    print("2.删除名片")
    print("3.修改")
    print("4.查询")
    print("5.所有")
    print("6.退出")
    print("--------------------------")
    a=input("请出入1-6进行选项的选择")
    if a==1:
        tianji()
    elif a==2:
        shanchu()
    elif a==3:
        xiugai()
    elif a==4:
        chaxun()
    elif a==5:
        suoyou()
    elif a==6:
        exit()
    else:
        print("输入的不是1-6请重新输出")
