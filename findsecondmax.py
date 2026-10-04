list=[1,2,3,4999,123]
First=0
second=0
for i in list:
    if i > First :
        second = First
        First = i
print("first",First ,"second",second)
        