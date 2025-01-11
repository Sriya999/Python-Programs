arr = [12, 35, 1, 10, 34, 1]
#better approach --tc :o(n)
maxi=arr[0]

for i in range(0,len(arr)):
    if arr[i]>maxi:
        maxi=arr[i]
        
secmaxi=-1

for i in range(0,len(arr)):
    if arr[i]>secmaxi and arr[i]!=maxi:
        secmaxi=arr[i]
        
print("second largest element:",secmaxi)