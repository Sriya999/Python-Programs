
#add using stacks

#number -> stack
def makestack(num):
    stack=[]
    for c in num:
        stack.append(c)
    return stack
#addition using stacks

def add_numstacks(n1,n2):
    carry=0#carry tp be forwarded
    s1=makestack(n1)
    s2=makestack(n2)
    res=[]
    while s1 or s2 or carry:
        d1=int(s1.pop()) if s1 else 0
        d2=int(s2.pop()) if s2 else 0
        total=d1+d2+carry
        res.append(total%10)
        carry=total//10
        
    ans=""
    while res:
        ans=ans+str(res.pop())
    return ans
    
n1=input()
n2=input()
print(add_numstacks(n1,n2))
      
    

