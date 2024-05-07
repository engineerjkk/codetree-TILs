import copy
from itertools import combinations_with_replacement,product
n= int(input())
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))

d=[[[-1,0],[-2,0],[1,0],[2,0]],
[[-1,0],[0,1],[1,0],[0,-1]],
[[-1,-1],[1,1],[-1,1],[1,-1]]
]
d_arr=[0,1,2]
tmp=[]
for i in range(n):
    for j in range(n):
        if lst[i][j]==1:
            tmp.append([i,j])
len_bomb=len(tmp)
#폭탄의 개수만큼 조합이 생긴다.
nCr=product(d_arr,repeat=len_bomb)

ans=0
for x in nCr: #조합 계산 len_bomb
    arr=[]
    arr=copy.deepcopy(lst)
    for k in range(len(tmp)):
        # 폭탄이 있는 방
        bomb_r=tmp[k][0]
        bomb_c=tmp[k][1]
        # 주변에 터질 폭탄
        for i in range(4):
            r=d[x[k]][i][0]
            c=d[x[k]][i][1]
            nr=bomb_r+r
            nc=bomb_c+c
            if -1<nr<n and -1<nc<n:
                arr[nr][nc]+=1
    cnt=0
    for i in range(n):
        for j in range(n):
            if arr[i][j]>0:
                cnt+=1
    ans=max(ans,cnt)

print(ans)