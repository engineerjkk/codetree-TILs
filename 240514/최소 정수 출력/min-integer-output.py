import sys
input = sys.stdin.readline
import heapq

pq=[]
n = int(input())
for _ in range(n):
    a=int(input())
    if a!=0:
        heapq.heappush(pq,a)
    else:
        if len(pq)==0:
            print(0)
        else:
            print(pq[0])
            heapq.heappop(pq)