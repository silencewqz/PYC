#
# try:
#     pass
#
#     a = input("请输入第一个数字")
#     a1 = input("请输入第二个数字")
#     print("加法法" + str((int(a) + int(a1))))
#     print("减法法" + str((int(a) - int(a1))))
#     print("乘法法" + str((int(a) * int(a1))))
#     print("幂法法" + str((int(a) ** int(a1))))
#     print("除法" + str((int(a) / int(a1))))
#     print("整除法" + str((int(a) // int(a1))))
# except():
#     pass
#
# # if a.isnumeric() and a1.isnumeric():
# #     if a<a1 :
# #         print("第二个大")
# #
# #     elif a==a1:
# #         print("相等")
# #     else:
# #         print("第一个大")
# # else:
# #     print("输入的不是数字")
# 异常处理
try:
    # 需要捕捉的代码]
    raise   Exception
    # '''手动处发异常'''
    pass
except Exception as e  :
    # 所有异常的父类
    print(e)
    pass

finally:
    # 无论是否报错都执行
    pass
