def binarys(arr,t):
    l,r=0,len(arr)-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==t:
            return mid
        elif arr[mid]<t:
            l=mid+1
        else:
           r=mid-1
    if r==-1:
        return 'a'#if there is no such element exists return a
    return arr[r]
    
arr=['d','e','g','k','y']
t='c'
print(binarys(arr,t))

