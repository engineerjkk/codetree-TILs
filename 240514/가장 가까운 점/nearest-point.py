import sys
input = sys.stdin.readline
import heapq

n, m = map(int,input().split())
pq=[]
for i in range(n):
    x,y= map(int,input().split())
    heapq.heappush(pq,(x+y,x,y))

for _ in range(m):
    c,a,b=heapq.heappop(pq)
    a+=2
    b+=2
    c=a+b
    heapq.heappush(pq,(c,a,b))

print(pq[0][1],end=" ")
print(pq[0][2])