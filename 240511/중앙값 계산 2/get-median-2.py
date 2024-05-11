import sys
input = sys.stdin.readline
n=int(input())
lst=list(map(int,input().split()))

tmp=[]
for i in range(n):
    tmp.append(lst[i])
    if lst[i]%2==1:
        sorted(tmp)
        idx=len(tmp)//2
        print(tmp[idx],end=" ")