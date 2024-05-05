import sys
input = sys.stdin.readline
n,m = tuple(map(int,input().split()))
A=list(map(int,input().split()))
B=list(map(int,input().split()))

set_A=set(A)
set_B=set(B)

ans=[]
for i in A:
    if i in set_B:
        ans.append(i)
for i in B:
    if i in set_A:
        ans.append(i)
print(len(list(set(ans))))