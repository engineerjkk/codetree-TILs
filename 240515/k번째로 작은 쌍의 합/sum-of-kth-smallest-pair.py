import heapq
import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
lst_n = list(map(int,input().split()))
lst_m = list(map(int,input().split()))

lst=[]
for i in range(n):
    for j in range(m):
        lst.append(lst_n[i]+lst_m[j])

lst.sort()#,key=lambda x:(x[0]+x[1]))
print(lst[k-1])