import sys
input = sys.stdin.readline
import heapq
n = int(input())
lst=list(map(int,input().split()))

for i in range(1,n-2):
    pq=[]
    for j in range(i,n):
        heapq.heappush(pq,lst[j])
    heapq.heappop(pq)
    # tmp=[]
    # while pq:
    #     tmp.append(heapq.heappop(pq))
print(f"{sum(pq)/len(pq):.2f}")