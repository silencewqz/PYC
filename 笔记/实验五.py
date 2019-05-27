list1=["皮","pi","sa"]
for i in list1:
    print("名{0}".format(i))
print("wxihuan pi")

list1=["cat","dog","ji"]
for i in list1:
    print("名字",format(i))
print("doushidxwu")

for i in range(1,21):
    print(i)
list2=[]
for i in range(1,100000):
     list2.append(i)
for i in list2:
   print(i)
print(min(list2))
print(max(list2))
print(sum(list2))
list3=[]
for i in range(1,21,2):
    list3.append(i)
for i in list3:
    print(i)
list3=[]
for i in range(3,31,30):
    list3.append(i)
for i in list3:
    print(i)
list4=[]
for i in range(1,11):
    list4.append(i**3)
for i in list4:
    print(i)
list5=list1
list1.append("sa")
list5.append("sdaf")
for i in list5:
    print(i)
for i in list1:
    print(i)


yuan=("rou","cai","fan","re","sa")
for i in yuan:
    print(i)
yuan=("rou","cai","fan","e","s")
for i in yuan:
    print(i)