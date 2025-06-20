#User function Template for python3
class Solution:
	def longestSubarrayDivK(self, arr, k):
		#Complete the function
		n=len(arr)
		rem_map={0:-1}
		maxlen=0
		prefixsum=0
		for i in range(n):
		    prefixsum=prefixsum+arr[i]
		    rem=prefixsum%k
		    #negative values
		    if rem<0:
		        rem=rem+k
		    if rem in rem_map:
		        maxlen=max(maxlen,i-rem_map[rem])
		    else:
		        rem_map[rem]=i
		return maxlen
		        
		    

