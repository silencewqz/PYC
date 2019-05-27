student=[{"number":"1","sex":"男","age":"12","姓名":"lao","phoneno":"12121"}]
# 查找是否重复
def chong(a):
    e=True
    for i in range(0,len(student)):
        if student[i]["number"]==a:
            e=False
    return e
# 打印菜单
def cai():
    print("--------------------------")
    print("    学生管理系统   v8.8")
    print("1.添加")
    print("2.删除")
    print("3.修改")
    print("4.查询")

    print("5.所有")
    print("6.退出")
    print("--------------------------")
    a = input("请出入1-6进行选项的选择")
    xuan(a)
    # 是否继续
def ji():
    aaaa = input("是否继续添加1继续2结束")
    if int(aaaa) == 1:
        return True
    elif int(aaaa) == 2:
       return False
    # 检测是为纯数字
def shu(a):
    if a.isdigit():
        return True
    else:
        return  False
    # 是否只为男女
def nannv(a):
    if a == "男" or a == "女":
       return True
    else:
      return False
    # 是否只为字符
def ming(a):
    if a.isalpha():
        return  True
    else:
        return False
    # 添加函数
def tianjia():

    while True:
        st = {}
        while True:
            a=input("请输入学号")
            if  shu(a):
                if chong(a):
                    st['number']=a
                    break
            else:
                print("学号内有数字请重新输入")
                continue
        while True:
            a=input("请输入性别")
            if  nannv(a):
                st['sex']=a
                break
            else:
                print("请重新输入性别 男或女")
                continue
        while True:
             a = input("请输入姓名")
             if ming(a):
                 st["姓名"]=a
                 break
             else:
                 print("信息有误")
                 continue
        while True:
            a = input("请输入手机号")
            if shu(a):
                st['phoneno']= a
                break
            else:
                print("手机号内有字符请重新输入")
                continue

        student.append(st)
        if ji():
            continue
        else:
            break
    # 删除函数
def shanchu():
    while  True:
        a=input('请输入要删除的学号')
        if shu(a):
            for i in range(0,len(student)):
                if student[i]["number"]==a:
                    print(student.pop(i))
                    break

        else:
            print("学号输入有误")
            continue
        if ji():
            continue
        else:
            break

# 修改函数
def xiugai():
    while True:
        a=input("请输入要修改的学号")
        if shu(a):

            for i in range(0, len(student)):
                if student[i]["number"] == a:
                        a = input("输入1修改学号，输入2修改性别，输入3修改年龄，输入4修改姓名，输入5修改电话")
                        if int(a) == 1:
                            a1 = input("请输入要修改的学号")
                            if shu(a1):
                                if chong(a1):
                                    student[i]["number"]=a1
                            else:
                                print("学号输入有误")
                        elif int(a)==2:
                            a1 = input("请输入要修改性别")
                            if nannv(a1):
                                student[i]["sex"] = a1
                            else:
                                print("性别输入有误")
                        elif int(a) == 3:
                            a1 = input("请输入要修改的年龄")
                            if shu(a1):
                                student[i]["age"] = a1
                            else:
                                print("年龄输入有误")
                        elif int(a)== 4:
                            a1 = input("请输入要修改的姓名")
                            if ming(a1):
                                student[i]["姓名"] = a1
                            else:
                                print("姓名输入有误")
                        elif int(a)== 5:
                            a1 = input("请输入要修改的电话")
                            if shu(a1):
                                student[i]["phoneno"] = a1
                            else:
                                print("电话号码有误")


        if ji():
            continue
        else:
             break
def xuan(a):
    if int(a)==1:
        tianjia()
        print(a)
    elif int(a)==2:
        shanchu()
    elif int(a)==3:
        xiugai()
    elif int(a)==4:
        cha()
    elif int(a)==5:
        suoyou()
    elif int(a)==6:
        exit()
    else:
        print("输入的不是1-6请重新输出")
def cha():

        while True:
            a = input('请输入要查询的学号2')
            if shu(a):
                for i in range(0, len(student)):
                    if student[i]["number"] == a:
                        print(student[i])
            else:
                print("学号输入有误2")
                continue
            if ji():
                continue
            else:
                break
def suoyou():
    for i in range(0, len(student)):
        print(student[i])
while True:
    cai()
