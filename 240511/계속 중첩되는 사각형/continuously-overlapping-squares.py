import sys
input = sys.stdin.readline
n=int(input())
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))

arr=[[0]*201 for _ in range(201)]

for i in range(n):
    x1,y1,x2,y2=lst[i]
    x1+=100
    y1+=100
    x2+=100
    y2+=100
    if i%2==0:
        for j in range(x1,x2):
            for k in range(y1,y2):
                arr[j][k]=1
    else:
        for j in range(x1,x2):
            for k in range(y1,y2):
                arr[j][k]=-1
ans=0
for i in range(201):
    for j in range(201):
        if arr[i][j]==-1:
            ans+=1
print(ans)