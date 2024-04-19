import sys
input = sys.stdin.readline
arr=list(map(int,input().strip()))

ans=0
if len(arr)>1:
    # for i in range(len(arr)):
    #     ans+=arr[i]*2**(len(arr)-i-1)
    for i in range(len(arr)):
        if arr[i]==0:
            arr[i]=1
        else:
            arr[i]=0
        tmp=0
        for j in range(len(arr)):
            tmp+=arr[j]*2**(len(arr)-j-1)
        ans=max(ans,tmp)
        if arr[i]==0:
            arr[i]=1
        else:
            arr[i]=0
else:
    if arr[0]==1:
        ans=0
    else:
        ans=1
        
print(ans)