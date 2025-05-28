def linearsch(a, idx):
    if idx >= len(a):
        return -1
    if a[idx] == key:
        return idx
    else:
        return linearsch(a, idx + 1)

# backward approach
def linearsearch(a, target, n):
    if n == 0:
        return -1
    elif a[n - 1] == target:
        return n - 1
    else:
        return linearsearch(a, target, n - 1)

a = [23, 45, 65, 89, 90]
key = 45
target = 65 
print(linearsch(a, 0))
