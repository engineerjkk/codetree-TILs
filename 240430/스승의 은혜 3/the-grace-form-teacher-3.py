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
    tmp=[]
    for j in range(n):
        tmp.append(lst[j])
    tmp[i][0]=tmp[i][0]/2
    cash=0
    cnt=0
    tmp_price = sorted(tmp, key=lambda x: x[0])
    for x in range(n):
        if cash+tmp_price[x][0]+tmp_price[x][1]>b:
            break
        cash+=tmp_price[x][0]
        cash+=tmp_price[x][1]
        cnt+=1
    ans=max(ans,cnt)

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