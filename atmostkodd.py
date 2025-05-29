nums = [1,1,2,1,1]
k = 3
l=0
temp=0
ans=0
for r in range(0,len(nums)):
    if nums[r]%2==1:
        temp+=1
    while temp>k:
        if nums[l]%2==1:
            temp=temp-1
        l+=1
    ans=ans+r-l+1
  
