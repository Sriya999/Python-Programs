nums=[1,0,0,1,0]
k=1
temp1=0
temp0=0
ans=0 
l=0
for i in range(0,len(nums)):
    if nums[i]==1:
        temp1+=1
    else:
        temp0+=1
    while min(temp1,temp0)>k:
        if nums[l]==0:
            temp0-=1
        else:
            temp1-=1
        l+=1
    ans=max(ans,i-l+1)

print(ans)
            
        
