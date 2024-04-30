import sys
input = sys.stdin.readline
n,b = map(int,input().split())
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))



ans=0
cnt=0
#lst.sort()
for i in range(n):
    for j in range(n):
        cash=0
        cnt=0
        if i==j:
            lst[i][0]=lst[i][0]/2
        for x in range(n):
            if cash+lst[x][0]+lst[x][1]>b:
                break
            cash+=lst[x][0]
            cash+=lst[x][1]
            cnt+=1
        ans=max(ans,cnt)
        lst[i][0]=lst[i][0]*2
print(ans)