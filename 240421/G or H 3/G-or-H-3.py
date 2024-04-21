import sys
input = sys.stdin.readline
n, k = map(int,input().split())
lst=[]
for _ in range(n):
    lst.append(map(str,input().split()))

tmp=[0]*10001
for i,cha in lst:
    if cha=="G":
        tmp[int(i)]=1
    elif cha=="H":
        tmp[int(i)]=2

ans=0
for i in range(len(tmp)-k):
    nm=0
    for j in range(i,i+k+1):
        nm+=tmp[j]
    ans=max(ans,nm)
print(ans)