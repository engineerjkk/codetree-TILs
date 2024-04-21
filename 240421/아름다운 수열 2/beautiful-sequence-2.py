import sys
input = sys.stdin.readline
from itertools import combinations
n,m = map(int,input().split())
n_lst=list(map(int,input().split()))
m_lst=list(map(int,input().split()))

nCr = combinations(n_lst,m)
cnt=0

for x in nCr:
    tmp=[]
    for i in x:
        tmp.append(i)
    if tmp == m_lst:
        cnt+=1

print(cnt)