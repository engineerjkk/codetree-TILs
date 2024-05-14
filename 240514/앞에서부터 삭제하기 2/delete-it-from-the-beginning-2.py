import sys
input = sys.stdin.readline
import heapq
n = int(input())
lst=list(map(int,input().split()))

ans=0
for i in range(1,n-2):
    pq=[]
    for j in range(i,n):
        heapq.heappush(pq,lst[j])
    heapq.heappop(pq)
    ans=max(ans,sum(pq)/len(pq))
    # tmp=[]
    # while pq:
    #     tmp.append(heapq.heappop(pq))
print(f"{ans:.2f}")