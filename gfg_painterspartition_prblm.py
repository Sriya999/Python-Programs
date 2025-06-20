#User function Template for python3

class Solution:
    def ispos(self,arr,k,maxtime):
        p=1
        t=0
        for b in arr:
            if b+t<=maxtime:
                t=t+b
            else:
                #new painter
                p=p+1
                t=b
        return p<=k
    def minTime (self, arr, k):
        #code here
        l=max(arr)
        r=sum(arr)
        while l<=r:
            m=l+(r-l)//2
            if self.ispos(arr,k,m):
                r=m-1
            else:
                l=m+1
        return l
        
        
