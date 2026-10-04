num=int(input("enter the number:"))
div=2
while div<=num:
    if num%div==0:
        # j=2
        # while j<=(div//2)+1:
        #     if div %j == 0:
        #         j+=1
        #         break
        #     else:
        #         j+=1
        #         print(j,end=' ')
        for j in range(2,(div//2)+1):
            if div%j==0:
                break
        else:
            print(div,end=" ")

    div+=1
