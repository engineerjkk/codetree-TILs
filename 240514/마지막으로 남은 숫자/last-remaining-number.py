import heapq
import sys
input = sys.stdin.readline

n = int(input())
lst=list(map(int,input().split()))
pq=[]
for i in lst:
    heapq.heappush(pq,-i)  

while len(pq)>=2:
    a = -heapq.heappop(pq)
    b = -heapq.heappop(pq)
    c=a-b
    if c !=0:
        heapq.heappush(pq,-c)
if len(pq)>0:
    print(-pq[0])
else:
    print(-1)