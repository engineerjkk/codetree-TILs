import sys
input = sys.stdin.readline
n=int(input())
lst=list(map(int,input().split()))

ans=0
for i in range(n):
    for j in range(i,n):
        tmp=[]
        for k in range(i,j+1):
            tmp.append(lst[k])
        if len(tmp):
            and2=sum(tmp)/len(tmp)
            if and2 in tmp:
                ans+=1
print(ans)