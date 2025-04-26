l=[-4,5,0,1,2,0,-6]
neg=[]
pos=[]
for i in range(0,len(l)):
    if l[i]<=0:
        neg.append(l[i])
    else:
        pos.append(l[i])

neg.sort()
res=pos+neg
for i in res:
    print(i,end=" ")
