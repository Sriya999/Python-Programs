import math

def  find_divisors(n):
    divisors=[]
    for i in range(1,int(math.sqrt(n))+1):
        if n%i==0:
            divisors.append(i)
            if i!=n/i:
                divisors.append(n/i)
    divisors.sort()

    return divisors

num=int(input("Enter any number:"))
result=find_divisors(num)

print(result)
