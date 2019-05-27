menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车站': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}
print("返回请输入返回，退出请输入退出 输入城市名进入下一级菜单")
list1=[]
while 1:
    if len(list1) < 1:
        print(list(menu.keys()))
        a = input("请输入城市")
        if a == "返回":
            continue
        elif a == "退出":
            exit()
        else:
            list1.append(a)
    elif len(list1)==1:
        print(list(menu[list1[0]].keys()))
        a = input("请输入城市")
        if a == "返回":
            list1.pop()
            continue
        elif a == "退出":
            exit()
        else:
            list1.append(a)
    elif len(list1) == 2:
        print(list(menu[list1[0]][list1[1]].keys()))
        a = input("请输入城市")
        if a=="返回":
            list1.pop()
            continue
        elif a=="退出":

            exit()
        else:
            list1.append(a)
    elif len(list1)==3:
        print(list(menu[list1[0]][list1[1]][list1[2]].keys()))
        ccc=input("已到最后一层请输入返回或者退出")
        if ccc=='返回':
            list1.pop()
            continue
        elif ccc=="退出":
            exit()



