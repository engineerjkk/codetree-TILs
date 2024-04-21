import sys
input = sys.stdin.readline
from itertools import combinations, combinations_with_replacement,permutations
n,m = map(int,input().split())
n_lst=list(map(int,input().split()))
m_lst=list(map(int,input().split()))

nCr = permutations(m_lst,m)
cnt=0

nCr=list(set(nCr))
test=[]
for i in nCr:
    tmp=[]
    for j in i:
        tmp.append(j)
    test.append(tmp)
for x in test:
    for i in range(n-m+1):
        tmp=[]
        for j in range(i,i+m):
            tmp.append(n_lst[j])
        if tmp==x:
            cnt+=1

print(cnt)