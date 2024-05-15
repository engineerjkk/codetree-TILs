import sys
input = sys.stdin.readline
import heapq

n=int(input())
lst=list(map(int,input().split()))

pq=[]
ans_lst=[]
for i in range(n):
    heapq.heappush(pq,lst[i])
    ans=1
    if len(pq)<=2:
        ans_lst.append(-1)
    else:
        for j in heapq.nsmallest(3,pq):
            ans*=j
        ans_lst.append(ans)

for i in ans_lst:
    print(i)