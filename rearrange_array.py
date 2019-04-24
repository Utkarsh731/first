num=int(input("enter the number of elements in the array"))
array=list(map(int,input().split()))
s=num//2
j=num-1
array.sort()
q=[]
if (num%2)!=0:
    for i in range(0,s):
        q.append(array[j])
        q.append(array[i])
        j-=1
    q.append(array[j])
    print(",".join(map(str,q)))    
else:
    for i in range(0,s):
        q.append(array[j])
        q.append(array[i])
        j-=1
    print(",".join(map(str,q)))
