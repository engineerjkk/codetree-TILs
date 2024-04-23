import sys
input = sys.stdin.readline

n=int(input())
work=[]
for _ in range(n):
    work.append(list(map(int,input().split())))


ans=0
for i in range(n):
    time=[0]*1001
    for j in range(n):
        if i==j:
            continue
        else:
            start,end=work[j]
            for k in range(start,end):
                time[k]=1
    total=sum(time)
    ans=max(ans,total)
print(ans)