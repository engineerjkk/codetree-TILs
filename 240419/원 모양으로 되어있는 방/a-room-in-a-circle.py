import sys
INT_MAX=sys.maxsize
input = sys.stdin.readline
from collections import deque
import copy
n=int(input())


nm=0
queue=deque()
for _ in range(n):
    queue.append(int(input()))
distance=INT_MAX
for i in range(n):
    queue2=copy.deepcopy(queue)
    dis=0
    for j in range(i):
        x=queue2.popleft()
        queue2.append(x)
    for j in range(n):
        dis+=queue2[j]*j
    distance=min(distance,dis)
print(distance)