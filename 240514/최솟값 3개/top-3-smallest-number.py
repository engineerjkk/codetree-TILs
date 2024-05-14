import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
lst=list(map(int,input().split()))

queue=[]
for i in range(n):
    queue.append(lst[i])
    if i <2:
        print(-1)
    else:
        ans=1
        queue.sort()
        for j in range(3):
            ans*=queue[j]
        print(ans)