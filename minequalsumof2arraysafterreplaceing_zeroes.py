
def equalsum(nums1,nums2):
    minSum=float('inf')
    
    cnt1=nums1.count(0)
    cnt2=nums2.count(0)
    #initializing  or replacing with min value-1 at zeroes
    sum1=sum(nums1)+cnt1
    sum2=sum(nums2)+cnt2
    if sum1==sum2:#if both sum equals
        return sum1
    if sum1>sum2:
        if cnt2>0:
            return sum1
        else:
            return -1
    if sum2>sum1:
        if cnt1>0:
            return sum2
        else:
            return -1
    
nums1 = [3,2,0,1,0]
nums2 = [6,5,0] 
print(equalsum(nums1,nums2))
