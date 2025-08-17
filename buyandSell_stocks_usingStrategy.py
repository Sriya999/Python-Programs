prices = [4,2,8]
strategy = [-1,0,1]
k = 2
#base
base_prof=0
for i in range(len(prices)):
    base_prof+=prices[i]*strategy[i]
print(base_prof)
maxprof=base_prof
n=len(prices)
#modifications
for r in range(n-k+1):
    l=r+k
    #org window sum
    org_sum=0
    for i in range(r,l):
        org_sum+=prices[i]*strategy[i]
    #modified window sum
    mod_wsum=0
    for j in range(r+k//2,l):#last k//2 becomes 1
        mod_wsum+=prices[j]*1
    maxprof=max(maxprof,base_prof-org_sum+mod_wsum)
        
print(maxprof)  
