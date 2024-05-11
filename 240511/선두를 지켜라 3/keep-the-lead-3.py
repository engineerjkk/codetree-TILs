n,m = map(int,input().split())
lst_A=[]
lst_B=[]
dis_A=[0]*(1000*1000+1)
dis_B=[0]*(1000*1000+1)
for _ in range(n):
    lst_A.append(list(map(int,input().split())))
for _ in range(m):
    lst_B.append(list(map(int,input().split())))

dis=0
cnt_A=0
for i in range(n):
    v,t=lst_A[i]
    for j in range(t):
        dis_A[cnt_A]=dis
        dis+=v
        cnt_A+=1

dis=0
cnt_B=0
for i in range(m):
    v,t=lst_B[i]
    for j in range(t):
        dis_B[cnt_B]=dis
        dis+=v
        cnt_B+=1
cnt=max(cnt_A,cnt_B)

ans=0
check=0
for i in range(cnt):
    if dis_A[i]>dis_B[i] and check!=1:
        check=1
        ans++1
    elif dis_A[i]<dis_B[i] and check!=2:
        check=2
        ans+=1
    elif dis_A[i]==dis_B[i] and check!=3:
        check=3
        ans+=1
print(ans)