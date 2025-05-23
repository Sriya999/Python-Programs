stack=[]
s=input()

for i in s:
    if i in "1234567890":
        stack.append(int(i))
    else:
        n2=stack.pop()
        n1=stack.pop()
        if i=='*':
            stack.append(n1*n2)
        elif i=='-':
            stack.append(n1-n2)
        elif i=='+':
            stack.append(n1+n2)
        elif i=='/':
            stack.append(n1/n2)

print(stack.pop())

    
#53+62/*35*+ 
#39
