
def onesubseq(i,res,sum1):
    
    if i>=3:
        #if condn is satisfied
        if sum1==2:
            print(res,"with sum:",sum1)
            return True
        #condition not satisfied
        return False
    res.append(s1[i])
    sum1+=s1[i]
    #pick
    
    if onesubseq(i+1,res,sum1):
        return True
    sum1=sum1-res.pop()
    if onesubseq(i+1,res,sum1):
        return True
    return False
s1=[1,2,1]
onesubseq(0,[],0)
