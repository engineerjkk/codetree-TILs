import sys
input = sys.stdin.readline
n, k = map(int,input().split())
lst = list(map(int,input().split()))

count={}
for elem in lst:
    if elem in count:
        count[elem]+=1
    else:
        count[elem]=1
ans_1st=0
ans_lst=[]
ans_cnt=[]
ans_cnt=0
ans_value=0
check=0
for i in range(k):
    ans_cnt=0
    ans_value=0
    for j in range(n):
        if lst[j] in count:
            if count[lst[j]] >= ans_cnt and lst[j] >= ans_value:
                ans_cnt=count[lst[j]]
                ans_value=lst[j]
    count.pop(ans_value,None)
    ans_lst.append(ans_value)

for i in ans_lst:
    print(i,end=" ")