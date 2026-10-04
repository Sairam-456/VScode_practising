nums= int(input("enter the number:" ))
count=2
count2=1
while count2<=nums:
    i=2
    count1=1
    while  i<=count:
        if count%i==0:
            count1+=1
        i+=1
    if count1<=2:
        print(count, end=" ")
        count2+=1
       
        

    count+=1
