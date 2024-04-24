# import sys
# input = sys.stdin.readline
n,k = tuple(map(int,input().split()))
lst=[]
for _ in range(n):
    lst.append(int(input()))

ans=0
for i in range(n):
    for j in range(i+1,n):
        if j-i>k:
            break
        if lst[i] !=lst[j]:
            continue
        ans=max(ans,lst[i])
print(ans)