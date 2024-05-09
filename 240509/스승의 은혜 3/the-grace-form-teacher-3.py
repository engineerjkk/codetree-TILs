import copy
n,b = map(int,input().split())
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))

ans=0
for i in range(n):
    arr=[]
    arr=copy.deepcopy(lst)
    arr[i][0]=arr[i][0]//2
    cash=0
    cheap=0
    cnt=0
    arr=sorted(arr,key=lambda x:(x[0]+x[1]))
    for j in range(n):
        if cash+arr[j][0]+cheap+arr[j][1]>b:
            break
        else:
            cash+=arr[j][0]
            cheap+=arr[j][1]
            cnt+=1
    ans=max(ans,cnt)
print(ans)