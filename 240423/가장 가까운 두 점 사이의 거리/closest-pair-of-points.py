import sys
input = sys.stdin.readline

n = int(input())
lines = []
for _ in range(n):
    lines.append(list(map(int,input().split())))

ans=sys.maxsize
for i in range(n):
    for j in range(i,n):
        if i==j:
            continue
        x1,y1=lines[i]
        x2,y2=lines[j]
        distance=abs(x1-x2)*abs(x1-x2)+abs(y1-y2)*abs(y1-y2)
        ans=min(ans,distance)
print(ans)