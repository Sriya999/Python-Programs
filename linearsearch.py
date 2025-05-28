
def linearsch(a):
    idx=0
    while idx<len(a):
        if a[idx]==key:
            return idx
            break
        idx=idx+1
    return -1

a=[23,45,65,89,90]
key=90
print(linearsch(a))
