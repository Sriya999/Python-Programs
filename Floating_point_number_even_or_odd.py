class Solution:
    def isEven(self, s):
        s = s.rstrip("0")
        
        s = s.rstrip(".")
        
        n = int(s[-1])
        
        
        return  n%2==0
    
    
if __name__=="__main__":
    s=input().strip()
    obj=Solution()
    ans=obj.isEven(s)
    
    if ans:
        print("EVEN")
    else:
        print("ODD")
    