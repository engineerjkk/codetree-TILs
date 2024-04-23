import sys
input = sys.stdin.readline
n = int(input())
points=[]
for _ in range(n):
    points.append(list(map(int,input().split())))

def check(i,j,k):
    check_x=False
    check_y=False
    for a in range(3):
        for b in range(a,3):
            if a==b:
                continue
            x1,y1=points[a]
            x2,y2=points[b]
            x=abs(x1-x2)
            y=abs(y1-y2)
            if x==0:
                check_x=True
            if y==0:
                check_y=True
    return check_x and check_y

def cal(i,j,k):
    x1,y1=points[i]
    x2,y2=points[j]
    x3,y3=points[k]
    return 0.5*abs((x1*y2+x2*y3+x3*y1)-(x2*y1+x3*y2+x1*y3))
answer=0 
for i in range(n):
    for j in range(i,n):
        for k in range(j,n):
            if check(i,j,k):
                ans=cal(i,j,k)
            answer=max(answer,ans*2)
print(int(answer))