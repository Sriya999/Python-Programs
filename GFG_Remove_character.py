class Solution:
    def removeChars (ob, string1, string2):
        # code here
        string2set=set(string2)
        res=""
        for i in range(0,len(string1)):
            if string1[i] not in string2set:
                res=res+string1[i]
                
        return  res