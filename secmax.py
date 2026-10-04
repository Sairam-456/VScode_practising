list=[999,2,3,99,123]
First=0
second=0
for i in list:
    if i > First :
        second = First
        First = i
    if i > second and i < First :
        second=i
print("first",First ,"second",second)
        