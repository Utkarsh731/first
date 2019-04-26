n=int(input())
l=[]
for i in range(0,n):
    l.append([])
    a,b=map(str,input().split())
    l[i].append(a)
    l[i].append(int(b))
l.sort(reverse=True)
l.sort(key = lambda x: x[1]) 
for i in range(n-1,-1,-1):
    print(l[i][0],end=" ")
    print(l[i][1])
    
