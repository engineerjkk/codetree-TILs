import sys
input = sys.stdin.readline
import copy
n,m,k = map(int,input().split())
lst=[]
ans=False
for _ in range(m):
    lst.append(int(input()))
tmp=[0]
for i in lst:
    tmp.append(i)
for i in range(k):
    for j,num in enumerate(lst):
        tmp[num]-=1
        if tmp[num]==0:
            print(num)
            exit()
print(-1)