rows=int(input("enter chay raa rows:"))
# for i in range(rows+1): #0
#     print(" "*(rows-i) + "*" *(2*i-1))
# for j in  range(rows-1,0,-1):
#     print(" "*(rows-j)+ "*"*(2*j-1))
i=rows
while i>=1:
    print(" "*(rows-i) + "*" *(2*i-1))
    i-=1 
j=0
while j<rows:
    print(" "*(rows-j-1) + "*" *(2*j+1))
    j+=1