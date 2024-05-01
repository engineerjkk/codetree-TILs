import sys
n,m=map(int,input().split())
lst_A=[]
for _ in range(n):
    lst_A.append(list(map(str,input().split())))

lst_B=[]
for _ in range(m):
    lst_B.append(list(map(str,input().split())))
MAX=sys.maxsize
tmp_A=[0]*100000
tmp_B=[0]*100000
i=0
cnt_A=0
pos_A=0
for i in range(n):
    direction, move= lst_A[i]
    move=int(move)
    if direction=='R':
        for j in range(1,move+1):
            cnt_A+=1
            pos_A+=1
            tmp_A[cnt_A]=pos_A
            
    elif direction=='L':
        for j in range(1,move+1):
            pos_A-=1
            cnt_A+=1
            tmp_A[cnt_A]=pos_A

cnt_B=0
pos_B=0
for i in range(m):
    direction, move= lst_B[i]
    move=int(move)
    if direction=='R':
        for j in range(1,move+1):
            cnt_B+=1
            pos_B+=1
            tmp_B[cnt_B]=pos_B

            
    elif direction=='L':
        for j in range(1,move+1):
            pos_B-=1
            cnt_B+=1
            tmp_B[cnt_B]=pos_B

threshold=max(cnt_B,cnt_A)
ans=False
for i in range(1,threshold+1):
    if tmp_A[i]==tmp_B[i]:
        ans=True
        break
if ans:
    print(i)
else:
    print(-1)