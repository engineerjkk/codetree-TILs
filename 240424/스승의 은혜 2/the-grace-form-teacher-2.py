import sys
input = sys.stdin.readline
n,b = map(int,input().split())
student=[]
for _ in range(n):
    student.append(int(input()))

for i in range(n):
    tmp=[]
    for j in range(n):
        tmp.append(student[j])
    if i==j:
        tmp[j]=tmp[j]/2
    
    cnt=0
    cash=0
    ans=0
    tmp.sort()
    for j in range(n):
        if cash+tmp[j]>b:
            break
        cash+=tmp[j]
        cnt+=1
    ans=max(ans,cnt)
print(cnt)