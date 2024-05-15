import heapq
import sys
INT_MAX=sys.maxsize
n=int(input())
ans=0
pq=[]
people=[]
for i in range(n):
    a,t=map(int,input().split())
    people.append((a,i+1,t))

people.append((INT_MAX,n+1,0))

people.sort()
exit_time=0

for a,num,t in people:
    while a > exit_time and pq:
        _,next_a,next_t=heapq.heappop(pq)
        ans=max(ans,exit_time-next_a)
        exit_time+=next_t
    
    if a > exit_time:
        exit_time=a+t
    else:
        heapq.heappush(pq,(num,a,t))
print(ans)