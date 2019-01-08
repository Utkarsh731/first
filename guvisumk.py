n,k=map(int,input().split())
if k>n:
    print("k cannot greater then n")
else:
    a=list(map(int,input().split()))
    s=0
    for i in range(0,k):
        s=s+a[i]
    print(s)
