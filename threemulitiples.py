nums=int(input("enter the number:"))
i=0
sum=0
while i<=nums:
    if i%3==0:
        sum+=i
    i+=1
print("sum of three mulitiples is :",sum)