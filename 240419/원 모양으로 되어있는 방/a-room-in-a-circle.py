import sys
INT_MAX=sys.maxsize
input = sys.stdin.readline
from collections import deque
n=int(input())


nm=0
queue=deque()
for _ in range(n):
    queue.append(int(input()))
distance=INT_MAX
for i in range(n):
    dis=0
    if i==0:
        continue
    else:       
        for j in range(i):
            x=queue.popleft()
            queue.append(x)
    for j in range(n):
        dis+=queue[j]*j
    distance=min(distance,dis)
print(distance)