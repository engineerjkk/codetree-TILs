import sys
input = sys.stdin.readline
n,k=map(int,input().split())
lst=list(map(int,input().split()))

SUM=0
for i in range(n-k+1):
    total=0
    for j in range(i,i+k):
        total+=lst[j]
    SUM=max(SUM,total)
print(SUM)