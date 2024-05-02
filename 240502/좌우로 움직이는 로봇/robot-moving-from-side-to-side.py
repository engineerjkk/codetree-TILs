n,m = map(int,input().split())
lstA=[]
for _ in range (n):
    lstA.append(list(map(str,input().split())))
lstB=[]
for _ in range(m):
    lstB.append(list(map(str,input().split())))

MAX=1,000,001

tmpA=[0]*MAX
tmpB=[0]*MAX
cntA=0
mvA=0
for i in range(n):
    t,d=lstA[i]
    t=int(t)
    for _ in range(t):
        cntA+=1
        if d=='R':
            mvA+=1
            tmpA[cntA]=mvA
        elif d=='L':
            mvA-=1
            tmpA[cntA]=mvA
for i in range(cntA+1,MAX):
    tmpA[i]=mvA
cntB=0
mvB=0
for i in range(m):
    t,d=lstB[i]
    t=int(t)
    for _ in range(t):
        cntB+=1
        if d=='R':
            mvB+=1
            tmpB[cntB]=mvB
        elif d=='L':
            mvB-=1
            tmpB[cntB]=mvB
for i in range(cntB+1,MAX):
    tmpB[i]=mvB

rng=max(cntA,cntB)
cnt=0
for i in range(1,rng-1):
    if tmpA[i]!=tmpB[i] and tmpA[i+1]==tmpB[i+1]:
        cnt+=1
print(cnt)