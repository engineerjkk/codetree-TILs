import sys
input = sys.stdin.readline
from collections import deque
n,m = map(int,input().split())
lst=list(map(int,input().split()))

ans=0
for i in range(n):
    arr=[]
    queue=deque()
    queue.append(lst[i])
    for j in range(m):
        q=queue.popleft()
        arr.append(q)
        queue.append(lst[q-1])
    value=sum(arr)
    ans=max(ans,value)
print(ans)