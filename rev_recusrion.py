def rev(arr,n):
    if n<0:
        return
    print(arr[n])
    rev(arr,n-1)
def rev2(i,arr,n):
    if i>=n//2:
        return
    arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
    rev2(i+1,arr,n)
arr=[1,2,3,4,5]
n=len(arr)
rev2(0,arr,n)
print(arr)
