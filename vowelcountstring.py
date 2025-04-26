s=input()
#consonantscount
ccount=0
#vowelcount
vcount=0
 
for i in s:
   if i in "aeiou":
      vcount=vcount+1
   else:
      ccount=ccount+1
print(ccount-vcount)
 
