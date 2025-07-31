def print_subseq(i,arr,res):
    if i>=len(arr):#base case
        print(res)
        return
    #pick
    res.append(arr[i])
    print_subseq(i+1,arr,res)
    res.pop()
    #not pick
    print_subseq(i+1,arr,res)
    
arr=[1,2,1]
print_subseq(0,arr,[])
