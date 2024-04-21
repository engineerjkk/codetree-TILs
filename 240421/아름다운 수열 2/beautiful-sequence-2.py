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
        tmp.append(str(j))
    test.append(''.join(tmp))
tmp=[]
for i in n_lst:
    tmp.append(str(i))
n_str_lst=''.join(tmp)
for i in range(n-m+1):
    for x in test:
        if n_str_lst[i:i+m]==x:
            cnt+=1
print(cnt)