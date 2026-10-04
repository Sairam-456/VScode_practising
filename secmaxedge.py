list=[0,0,0,0,2,0,3,0,-1,-3,-4,-2,-5,-99]
First=list[0]
second=list[3]
for i in list:
    if i > First :
        second = First
        First = i
        # print(First,second)
    if i > second and i < First :
        second=i
print("first",First ,"second",second)
        