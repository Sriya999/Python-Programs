
def countsubseq(i,sum1):
    if i>=3:
        #if condn is satisfied
        if sum1==3:
            return 1
        #condition not satisfied
        return 0
    sum1+=s1[i]
    #pick
    l=countsubseq(i+1,sum1)
    sum1=sum1-s1[i]
    #not pick
    r=countsubseq(i+1,sum1)
    return l+r
s1=[1,2,1]
print(countsubseq(0,0))
