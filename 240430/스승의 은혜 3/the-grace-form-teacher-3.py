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
    cash=0
    cnt=0
    tmp=[]
    for j in range(n):
        tmp.append(lst[j])
        
    tmp[i][0]=lst[i][0]/2
    tmp.sort()
    for x in range(n):
        if cash+tmp[x][0]+tmp[x][1]>b:
            break
        cash+=tmp[x][0]
        cash+=tmp[x][1]
        cnt+=1
    ans=max(ans,cnt)
print(ans)