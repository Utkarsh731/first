
n=int(input("enter the number of rows in diamond"))
q=0
for i in range(n,0,-1):
    print(" "*(i-1),end=" ")
    q+=1
    for j in range(0,q):
        print("*",end=" ")
    print()
for i in range(1,n+1):
    print(" "*(i-1),end=" ")
    q+=1
    for j in range(i,n+1):
        print("*",end=" ")
    print()
    
    
    
