import sys
input = sys.stdin.readline

n,m = map(int,input().split())

#각 줄마다 어떤 속도 v 로 몇 시간 t 동안 이동했는지 
lstA=[]
lstB=[]
for _ in range(n):
    lstA.append(list(map(int,input().split())))
for _ in range(m):
    lstB.append(list(map(int,input().split())))

arrA=[0]*(1000*1000+1)
cntA=0
disA=0
for i in range(len(lstA)):
    v,t = lstA[i]
    for j in range(t):
        cntA+=1
        disA+=v
        arrA[cntA]=disA

arrB=[0]*(1000*1000+1)
cntB=0
disB=0
for i in range(len(lstB)):
    v,t = lstB[i]
    for j in range(t):
        cntB+=1
        disB+=v
        arrB[cntB]=disB

rng=max(cntB,cntA)

final=[]
cnt=0
check=0
for i in range(1,rng):
    a=arrA[i]
    b=arrB[i]
    if a>b and check!=1:
        final.append(a)
        check=1
        cnt+=1
    elif b>a and check !=2:
        final.append(b)
        check=2
        cnt+=1
    elif a==b and check !=3:
        final.append((a,b))
        check=3
        cnt+=1
print(cnt)