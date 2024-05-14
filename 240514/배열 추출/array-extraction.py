import sys
input = sys.stdin.readline
import heapq

n = int(input())
pq=[]
for _ in range(n):
    a=int(input())
    if a!=0:
        heapq.heappush(pq,-a)
    else:
        if len(pq)!=0:
            print(-heapq.heappop(pq))
        else:
            print(0)