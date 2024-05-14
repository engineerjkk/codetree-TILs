import heapq
import sys
input = sys.stdin.readline

n = int(input())
lst=list(map(int,input().split()))

sum_avg=0
ans=0

sum_avg+=lst[n-1]
pq=[]
heapq.heappush(pq,lst[n-1])

for i in range(n-2,0,-1):
    heapq.heappush(pq,lst[i])
    sum_avg+=lst[i]
    min_val=pq[0]
    avg=(sum_avg-min_val)/(n-i-1)
    ans=max(ans,avg)
print(f"{ans:.2f}")