
def printnto_1(i,n):
    if i>n:
        return
    printnto_1(i+1,n)
    print(i)
n=int(input())
printnto_1(1,n) 
