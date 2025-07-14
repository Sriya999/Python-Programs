
def printname(i,n):
    if i<1:
        return
    print(i)
    printname(i-1,n)
n=int(input())
printname(n,n)
