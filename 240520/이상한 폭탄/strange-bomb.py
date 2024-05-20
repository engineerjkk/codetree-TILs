import sys
input = sys.stdin.readline
import heapq
n,k = tuple(map(int,input().split()))
lst=[]
for _ in range(n):
    lst.append(int(input()))

dic={}
ans=[]
for i in range(n-k):
    for j in range(i+1,i+k+1):

        if lst[i]==lst[j]:
            heapq.heappush(ans,-lst[i])
print(-ans[0])