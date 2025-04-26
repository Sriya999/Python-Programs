def is_PerfectNum(n):
    sum1=1
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
          sum1=sum1+i
          if i!=n//i:
            sum1=sum1+n//i
    if sum1==n:
        return True
    else:
        return False
def is_Prime(n):
    flag=True
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            flag=False
    return flag 
#array list input
arr=list(map(int,input().split()))
res=0
for i in arr:
    if is_PerfectNum(i) or is_Prime(i):
        res=res+i
print(res)   
  
