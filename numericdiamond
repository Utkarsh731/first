n=int(input("enter the number of rows in diamond"))
q=1
a="1"
l=[]
for i in range(n,1,-1):
    print(" "*(i-2),end=" ")
    q+=1
    print(a,end=" ")
    l.append(a)
    a=a+str(q)
    a=str(q)+a
    print()
for j in range(1,n-1):
    print(" "*(j+1),end="")
    print(l[n-j-2])
