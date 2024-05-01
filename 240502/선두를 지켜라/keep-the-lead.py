n,m = map(int,input().split())
lst_A=[]
lst_B=[]
for _ in range(n):
    lst_A.append(list(map(int,input().split())))
for _ in range(m):
    lst_B.append(list(map(int,input().split())))
MAX=1000001
arr_A=[0]*MAX
arr_B=[0]*MAX

cnt_A=0
dis=0
for v,t in lst_A:
    for i in range(t):
        cnt_A+=1
        dis+=v
        arr_A[cnt_A]=dis
cnt_B=0
dis=0
for v,t in lst_B:
    for i in range(t):
        cnt_B+=1
        dis+=v
        arr_B[cnt_B]=dis
ans=0
cnt=0
tmp=True

leader,ans=0,0
for i in range(1,cnt_B):
    if arr_A[i]>arr_B[i]:
        if leader==2:
            ans+=1
        leader=1
    elif arr_A[i]<arr_B[i]:
        if leader==1:
            ans+=1
        leader=2
print(ans)