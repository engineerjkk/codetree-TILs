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
ans=0
for i in range(k):
    for j in range(n):
        if lst[j] in count:
            if count[lst[j]] >= ans:
                ans=count[lst[j]]
                ans_1st=lst[j]
    count.pop(ans_1st,None)
    ans_cnt.append((ans_1st,ans))

ans_lst = sorted(ans_cnt, key = lambda x : (x[1], x[0]),reverse=True)

for i in ans_lst:
    print(i[0],end=" ")