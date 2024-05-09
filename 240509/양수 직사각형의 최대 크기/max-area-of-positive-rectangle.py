import sys
input = sys.stdin.readline
n,m = map(int,input().split())
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))
arr=[]
ans=-1

def rect(x1,y1,x2,y2):
    arr=[]
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if lst[i][j]>0:
                arr.append(1)
            else:
                arr.append(0)
    return all(arr)

for i in range(n):
    for j in range(m):
        for k in range(i,n):
            for l in range(j,m):
                if rect(i,j,k,l):
                    value=(k-i+1)*(l-j+1)
                    ans=max(value,ans)
print(ans)