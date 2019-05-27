gong=[{"hao":"1","qian":"100"}]
def shu(a):
    if a.isdigit():
        return True
    else:
        return  False
def ming(a):
    if a.isalpha():
        return  True
    else:
        return False
def chong(a):
    e=True
    for i in range(0,len(gong)):
        if gong[i]["number"]==a:
            e=False
    return e
def ji():
    aaaa = input("是否继续添加1继续2结束")
    if int(aaaa) == 1:
        return True
    elif int(aaaa) == 2:
       return False
while True:
    print("1.查询员工工资")
    print("2.修改员工工资")
    print("3.增加新员工记录")
    print("4.退出")
    a=input("请选择你的服务")
    if int(a)==1:
        while True:
            a=input("请输入查询的工号")
            if shu(a):
                for i in range(0, len(gong)):
                    if gong[i]["hao"] == a:
                        print(gong[i])
            if ji():
                continue
            else:
                break
    elif int(a)==2:
        while True:
            a = input("请输入修改的工号")
            if shu(a):
                for i in range(0, len(gong)):
                    if gong[i]["hao"] == a:
                        print(gong[i])
                        b=input("请输入要修改的金额")
                        gong[i]["qian"]=b
            if ji():
                continue
            else:
                break
    elif int(a) == 3:
        while True:
            a = input("请输入增加的工号")
            if shu(a):
                st={}
                b=input("请输入工号")
                if chong(b):
                    st["name"]=b
                    b = input("请输入工资")
                    st["qian"]=b
            if ji():
                continue
            else:
                break
    elif int(a)==4:
        exit()
