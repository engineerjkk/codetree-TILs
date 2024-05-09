import sys
INT_MAX = sys.maxsize
n,s = tuple(map(int,input().split()))
arr = list(map(int,input().split()))
array_sum=0
ans=INT_MAX
arr_sum=sum(arr)

for i in range(n):
    for j in range(i+1,n):
        if i==j:
            continue
        else:
            new_sum=arr_sum-arr[i]-arr[j]
            diff = abs(new_sum-s)
            ans=min(ans,diff)
print(ans)