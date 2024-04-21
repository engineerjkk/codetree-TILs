import sys
input = sys.stdin.readline
from itertools import combinations, combinations_with_replacement,permutations
n,m = map(int,input().split())
n_lst=list(map(int,input().split()))
m_lst=list(map(int,input().split()))

nCr = permutations(m_lst,m)
cnt=0

nCr=list(set(nCr))
for x in nCr:
    tmp2=[]
    for k in x:
        tmp2.append(k)
    for i in range(n-m+1):
        tmp=[]
        for j in range(i,i+m):
            tmp.append(n_lst[j])
        if tmp==tmp2:
            cnt+=1

print(cnt)