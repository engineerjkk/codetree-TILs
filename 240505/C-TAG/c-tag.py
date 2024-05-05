import sys
input = sys.stdin.readline
n,m = tuple(map(int,input().split()))
A=[]
for _ in range(n):
    A.append(input())
B=[]
for _ in range(n):
    B.append(input())
s=set()

def cal(x,y,z):
    s.clear()
    for i in range(n):
        s.add(A[i][x]+A[i][y]+A[i][z])
    for i in range(n):
        if (B[i][x]+B[i][y]+B[i][z]) in s:
            return False
    return True


ans=0
for i in range(m):
    for j in range(i+1,m):
        for k in range(j+1,m):
            if cal(i,j,k):
                ans+=1
print(ans)