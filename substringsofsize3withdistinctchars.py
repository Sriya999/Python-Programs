def isvalid(str1,sl):
    s1=set()
    for i in str1:
        s1.add(i)
    if len(s1)==sl:
        return True
    else:
        return False

str1="abzzzaa"
sl=3
count=0
for i in range(len(str1)-sl+1):
    res=isvalid(str1[i:i+3],sl)
    if res==True:
        count=count+1
print(count)

 
 
    
        
            
