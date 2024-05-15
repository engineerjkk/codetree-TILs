import sys
input = sys.stdin.readline
import heapq

n=int(input())
lst=list(map(int,input().split()))

pq=[]
ans_lst=[]
for i in range(n):
    heapq.heappush(pq,lst[i])
    if i<2:
        ans_lst.append(-1)
    else:
        tmp=[]
        ans=1
        for j in range(3):
            tmp.append(heapq.heappop(pq))
        for j in range(3):
            ans*=tmp[j]
            heapq.heappush(pq,tmp[j])
        ans_lst.append(ans)

for i in ans_lst:
    print(i)