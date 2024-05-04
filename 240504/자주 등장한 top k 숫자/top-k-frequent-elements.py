import sys
input = sys.stdin.readline
n, k = map(int,input().split())
lst = list(map(int,input().split()))

count={}
for i in lst:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
sorted(count.items(), key = lambda item: item[1],reverse=True)
answer={}
for key, value in count.items():
    if value in answer:
        answer[value].append(key)
    else:
        answer[value]=[key]
count={}
ans_lst=[]
cnt=0

while True:
    for key, value in answer.items():
        tmp_lst=[]
        for i in value:
            tmp_lst.append(i)
        tmp_lst=sorted(tmp_lst,reverse=True)
        for i in tmp_lst:
            print(i,end=" ")
            cnt+=1
            if cnt==k:
                exit()

    

# ans_cnt=0
# ans_value=0
# ans_lst=[]
# for i in range(k):
#     ans_cnt=0
#     ans_value=0
#     for j in lst:
#         if j in count and j >= ans_cnt and lst[j] >= ans_value:
#             ans_cnt=count[lst[j]]
#             ans_value=lst[j]
#     count.pop(ans_value,None)
#     ans_lst.append(ans_value)

# for i in ans_lst:
#     print(i,end=" ")