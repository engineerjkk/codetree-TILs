import sys
input = sys.stdin.readline
import copy
n,b = map(int,input().split())
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))

ans=0
cnt=0
for i in range(n):
    tmp=copy.deepcopy(lst)
    # tmp=[]
    # for j in range(n):
    #     tmp.append(lst[j])
    
    tmp[i][0]=tmp[i][0]//2
    cash=0
    cnt=0
    #tmp_price = sorted(tmp, key=lambda x: x[0])
    tmp.sort()
    for x in range(n):
        if cash+tmp[x][0]+tmp[x][1]>b:
            break
        cash+=tmp[x][0]
        cash+=tmp[x][1]
        cnt+=1
    if cnt>ans:
        ans=cnt

    # tmp_cheap = sorted(tmp, key=lambda x: x[1])
    # cnt=0
    # cash=0
    # for x in range(n):
    #     if cash+tmp_cheap[x][0]+tmp_cheap[x][1]>b:
    #         break
    #     cash+=tmp_cheap[x][0]
    #     cash+=tmp_cheap[x][1]
    #     cnt+=1
    # ans=max(ans,cnt)
print(ans)