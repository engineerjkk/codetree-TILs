import heapq
import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
lst_n = list(map(int,input().split()))
lst_m = list(map(int,input().split()))

lst=[]
hq=[]
for i in range(n):
    for j in range(m):
        heapq.heappush(hq,lst_n[i]+lst_m[j])
for i in range(k-1):
    heapq.heappop(hq)
print(hq[0])