def print_subseq(i,arr,res,sum1):
    if i>=len(arr):#base case
        if sum1==3:
            print(res)
        return
    #pick
    res.append(arr[i])
    sum1=sum1+arr[i]
    print_subseq(i+1,arr,res,sum1)
    
    sum1=sum1-res.pop()
    #not pick
    print_subseq(i+1,arr,res,sum1)
    
arr=[1,2,1,3]
print_subseq(0,arr,[],0)
