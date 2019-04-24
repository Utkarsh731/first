st=list(map(str,input().split()))
q=[]
c=0
last=st[len(st)-1]
if last[-1]=="." or last[-1]=="?":
    st[len(st)-1]=last[:len(last)-1]
    st.append(last[-1])
    c+=1
for i in st:
    if i not in q:
        q.append(i)
if c==0:
    print(*q)
else:
    for i in range(0,len(q)-2):
        print(q[i],end=" ")
    print(q[len(q)-2],end="")
    print(q[len(q)-1])
    
