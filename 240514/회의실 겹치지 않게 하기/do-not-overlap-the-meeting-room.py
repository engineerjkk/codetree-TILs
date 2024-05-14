import sys
input = sys.stdin.readline
from itertools import combinations
import copy
n = int(input())
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))

arr=[0]*100001
sorted_lst=sorted(lst)
idx_lst=[]
for i in range(n):
    idx_lst.append(i)
ans=100001
for i in range(n):
    nCr=combinations(idx_lst,i)
    for x in nCr:
        arr=[0]*100001
        check=True
        tmp_lst=copy.deepcopy(sorted_lst)
        for j in x:
            idx_lst.remove(j)
        cnt=0
        for j in idx_lst:
            start,end=sorted_lst[j]
            for k in range(start,end+1):
                arr[j]+=1
                cnt+=1
        for j in range(cnt):
            if arr[j]>1:
                check=False
        if check==True:
            ans=min(ans,i)
print(ans)