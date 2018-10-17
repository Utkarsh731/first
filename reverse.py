a=input()
def rev(a):
    b=''
    c=len(a)
    while(c>0):
        b=b+a[c-1]
        c=c-1

    return b
print(rev(a))
