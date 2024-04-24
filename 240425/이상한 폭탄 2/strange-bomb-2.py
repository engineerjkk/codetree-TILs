import sys
input = sys.stdin.readline
n,k=map(int,input().split())
bom=[]
for _ in range(n):
    bom.append(int(input()))

ans=-1
for i in range(n):
    for j in range(i+1,n):
        if i-j>k:
            break

        if bom[i]!=bom[j]:
            continue

        ans=max(ans,bom[i])
print(ans)