import sys
input=sys.stdin.readline
n,b=map(int,input().split())
students=[]
for _ in range(n):
    students.append(int(input()))

ans=0
for i in range(n):

    tmp=[]
    for j in range(n):
        tmp.append(students[j])

    tmp[i]=tmp[i]/2
    tmp.sort()
    cnt=0
    cash=0
    for j in range(n):
        if cash+tmp[j]>b:
            break
        cash+=tmp[j]
        cnt+=1
    ans=max(ans,cnt)
print(ans)