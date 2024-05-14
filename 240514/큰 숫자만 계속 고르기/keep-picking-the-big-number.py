import heapq
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
lst=list(map(int,input().split()))

pq=[]
for i in range(n):
    heapq.heappush(pq,-lst[i])

for i in range(m):
    a=-heapq.heappop(pq)
    #print(a)
    heapq.heappush(pq,-(a-1))
print(-pq[0])