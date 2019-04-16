
n=int(input("enter the number of rows in diamond"))
for i in range(0,n):
    print("*"*(n-i),end="")
    print(" "*(2*i+1),end="")
    print("*"*(n-i))
for i in range(n-2,-1,-1):
    print("*"*(n-i),end="")
    print(" "*(2*i+1),end="")
    print("*"*(n-i))
    
