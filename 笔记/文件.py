import  pickle
with open(r'text1.txt','r') as a:
    '''对文件进行操作'''
    aa = a.readline();'''按行读取'''
    while aa:
        print(aa)
        aa=a.readline();'''按行读取'''
    l=list(a);'''直接按行读取为一个列表'''
    a.read(1);'''每次读几个函数'''
    a.seek(4,0)
    a.tell();'''读取的位置'''
    a.write("aa");'''写操作'''
    a.writelines("aa");'''写一行操作'''
with open(r'text1.txt','r') as a:
    pickle.dump(1 ,a);'''保存类'''
    pickle.load(a);'''保存类'''
