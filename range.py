L=10
R=11
n=22
sum1=0
if L>R:
 print(0)
else:
    for i in range(L,R+1):
        sum1=sum1+i
    if sum1==n:
        print("neutral")
    elif sum1>n:
        less=sum1-n
        print("decrease "+str(less))
    elif sum1<n:
        more=n-sum1
        print("add "+str(more))
