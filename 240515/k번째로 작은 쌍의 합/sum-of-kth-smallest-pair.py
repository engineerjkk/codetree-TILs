import heapq
import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
lst_n = list(map(int,input().split()))
lst_m = list(map(int,input().split()))

lst=[]
pq=[]
for i in range(n):
    for j in range(m):
        heapq.heappush(pq,lst_n[i]+lst_m[j])
#print(pq)
print(heapq.nsmallest(k,pq)[-1])