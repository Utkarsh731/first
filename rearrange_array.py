num=int(input("enter the number of elements in the array"))
array=list(map(int,input().split()))
s=num//2
j=num-1
array.sort()
if (num%2)!=0:
    for i in range(0,s):
        print(array[j],end=",")
        print(array[i],end=",")
        j-=1
    print(array[s])
else:
    for i in range(0,s-1):
        print(array[j],end=",")
        print(array[i],end=",")
        j-=1
    print(array[j],end=",")
    print(array[s-1])
