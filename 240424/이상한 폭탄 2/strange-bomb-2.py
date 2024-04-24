# import sys
# input = sys.stdin.readline
n,k = map(int,input().split())
lst=[]
for _ in range(n):
    lst.append(int(input()))

ans=0
tmp=[]
for i in range(n):
    for j in range(n):
        if i==j:
            continue
        if lst[i]==lst[j]:
            if lst[i]>=abs(i-j):
                ans=max(ans,lst[i])
print(ans)