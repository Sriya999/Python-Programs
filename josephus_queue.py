from collections import deque
def josephus(n,k):
    q=deque(range(1,n+1))
    while len(q)>1:
        for i in range(k-1):
            q.append(q.popleft())
        q.popleft()
    return q[0]
n=int(input())#size
k=int(input())#kth person to  be eliminated
print(josephus(n,k))
