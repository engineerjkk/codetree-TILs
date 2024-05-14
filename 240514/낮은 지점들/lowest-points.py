import sys
input = sys.stdin.readline
n = int(input())
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))

hsh={}
for x,y in lst:
    if x in hsh:
        if hsh[x]>y:
            hsh[x]=y
    else:
        hsh[x]=y

ans=0
for key,value in hsh.items():
    ans+=value
print(ans)