try:
    a=int(input())
    c=0
    while a != 0:
        c=c+1
        a=a//10
    print(c)
except ValueError:
    print("Invalid Input")
