a={'f':"a",'q':"b",'b':"da",'c':"aaa"}
for key,value in a.items():
    print(key+":"+str(value))
aa=[{'f':"a",'q':"b",'b':"da",'c':"aaa"},{'fa':"a",'aq':"b",'sb':"da",'ffc':"aaa"},{'ff':"a",'qq':"b",'bb':"da",'cc':"aaa"}]
for i in aa:
    for key, value in i.items():
        print(key + ":" + str(value))

a={'f':"1",'q':"2",'b':"3",'c':"1"}
for key,value in a.items():
    print("姓名"+key+"喜欢的数字"+str(value))

a={'f':"1，5",'q':"2，1",'b':"3，1",'c':"1，4"}
for key,value in a.items():
    print("姓名"+key+"喜欢的数字"+str(value))


aa=[{'狗':"a"},{'猫':"a"}]
for i in aa:
    for key, value in i.items():
        print(key + ":" + str(value))

aa = [{'狗': "a,b"}, {'猫': "a,c"}]
for i in aa:
    for key, value in i.items():
        print(key + ":" + str(value))
aa={'shan':{"co":"a","po":"aa","fa":"sa"},'bei':{"co":"a","po":"aa","fa":"sa"},"guang":{"co":"a","po":"aa","fa":"sa"},}
for i in aa.keys():
    print(i)
    for key, value in aa[i].items():
        print(key + ":" + str(value))