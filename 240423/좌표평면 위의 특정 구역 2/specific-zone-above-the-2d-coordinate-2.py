import sys
input= sys.stdin.readline
n=int(input())
space=[]
for _ in range(n):
    space.append(list(map(int,input().split())))


ans=sys.maxsize
for i in range(n):
    row=[]
    col=[]
    for j in range(n):
        if i==j:
            continue
        x,y=space[j]
        row.append(x)
        col.append(y)
    x_max=max(row)
    x_min=min(row)
    y_max=max(col)
    y_min=min(col)
    rec=(x_max-x_min)*(y_max-y_min)
    ans=min(ans,rec)
print(ans)