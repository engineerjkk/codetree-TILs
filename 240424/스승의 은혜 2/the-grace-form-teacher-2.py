import sys
input = sys.stdin.readline
n,b = map(int,input().split())
student=[]
for _ in range(n):
    student.append(int(input()))



ans=0
for i in range(n):
    for j in range(n):
        for k in range(i,j+1):
            cash=0
            for l in range(i,k+1):
                if l==k:
                    cash+=(student[l]//2)
                else:
                    cash+=student[l]

            if b>=int(cash):
                ans=max(ans,k-i+1)
print(ans)