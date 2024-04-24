import sys
input = sys.stdin.readline
n, k = map(int,input().split())

bomb=[]
for _ in range(n):
    bomb.append(int(input()))

ans=-1
for i in range(n):
    for j in range(i+1,n):
        if abs(j-i)>k:
            break
        if i==j:
            continue
        if bomb[i]==bomb[j]:
            ans=max(ans,bomb[i])
print(ans)