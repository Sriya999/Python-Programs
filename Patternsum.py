h=int(input())
sum1=0
for i in range(1,h+1):
    for l in range(i,0,-1):
        print(l,end=" ")
        sum1+=l
    for j in range(2,i+1):
        print(j,end=" ")
        sum1+=j
    print()
print(sum1)
