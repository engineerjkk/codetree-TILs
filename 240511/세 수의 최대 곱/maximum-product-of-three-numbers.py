import sys
input = sys.stdin.readline
n=int(input())
lst=list(map(int,input().split()))

tmp=sorted(lst)
tmp1=1
tmp2=1

for i in range(1,4):
    tmp1*=tmp[-i]
for i in range(2):
    tmp2*=tmp[i]
tmp2*=tmp[-1]
print(max(tmp1,tmp2))