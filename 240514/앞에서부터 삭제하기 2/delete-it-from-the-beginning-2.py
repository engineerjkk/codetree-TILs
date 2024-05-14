import sys
input = sys.stdin.readline
import heapq
import copy
n = int(input())
lst=list(map(int,input().split()))

ans=0
for i in range(1,n-2):
    tmp=copy.deepcopy(lst)
    for j in range(i):
        tmp.pop(0)
    pq=copy.deepcopy(tmp)
    heapq.heapify(pq)
    heapq.heappop(pq)
    ans=max(ans,sum(pq)/len(pq))
    # tmp=[]
    # while pq:
    #     tmp.append(heapq.heappop(pq))
print(f"{ans:.2f}")