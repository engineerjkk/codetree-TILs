import sys
input = sys.stdin.readline
n,k = map(int,input().split())
lst=[]
for _ in range(n):
    lst.append(list(map(str,input().split())))
tmp=[]
for i in range(n):
    tmp.append(int(lst[i][0]))
MIN=min(tmp)
MAX=max(tmp)
MAX=100000
space=[0]*(MAX+1)
for i,name in lst:
    if name=='G':
        space[int(i)]=1
    elif name=='H':
        space[int(i)]=2
total=0

for i in range(MAX-k+1):
    cnt=0
    for j in range(i,i+k+1):
        cnt+=space[j]
    total=max(total,cnt)
print(total)