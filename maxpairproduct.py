arr=[20,16,2,1,5]
s1=set(arr)
maxprod=float('-inf')
for x in s1:
    diff=18-x
    if diff in s1:
        if x>diff:
            prod=diff*x
            maxprod=max(maxprod,prod)
print(maxprod)
            
        
