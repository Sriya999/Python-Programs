def priority(c):
    if c=='^':
        return 3
    elif c in ['/','*']:
        return 2
    elif c in ['+','-']:
        return 1
    else:
        return -1
def infix_to_postfix(exp):
    res=""
    stack=[]
    for i in exp:
        if i.isalnum():
            res=res+i
        elif i=='(':
            stack.append("(")
        elif i==')':
            while stack and stack[-1]!='(':
                res=res+stack.pop()
            stack.pop()
        else:
            while stack and  priority(i)<=priority(stack[-1]):
                res=res+stack.pop()
            stack.append(i)
    while stack:
        res=res+stack.pop()
    print(res)
            
            
exp=input()
infix_to_postfix(exp)
