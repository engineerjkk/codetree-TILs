def greedy(arr):
    count=0
    start_time=0
    for time in arr:
        if time[0] >= start_time:
            count+=1
            start_time = time[1]
    return count

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
arr.sort(key=lambda x : (x[1],x[0]))
print(n-greedy(arr))

# # import sys
# # input = sys.stdin.readline
# # from itertools import combinations
# # import copy
# # n = int(input())
# # lst=[]
# # for _ in range(n):
# #     lst.append(list(map(int,input().split())))

# # arr=[0]*100001
# # sorted_lst=sorted(lst)
# # idx_lst=[]
# # for i in range(n):
# #     idx_lst.append(i)
# # ans=100001
# # for i in range(n):
# #     nCr=combinations(idx_lst,i)
# #     for x in nCr:
# #         arr=[0]*100001
# #         check=True
# #         tmp_lst=copy.deepcopy(sorted_lst)
# #         for j in x:
# #             idx_lst.remove(j)
# #         cnt=0
# #         for j in idx_lst:
# #             start,end=sorted_lst[j]
# #             for k in range(start,end+1):
# #                 arr[j]+=1
# #                 cnt+=1
# #         for j in range(cnt):
# #             if arr[j]>1:
# #                 check=False
# #         if check==True:
# #             ans=min(ans,i)
# # print(ans)

# n = int(input())
# lst = []
# count = 1
# for i in range(n):
#     a, b=map(int,input().strip().split())
#     if a<=b:# 시간이 의미 있는 얘들만 뽑습니다
#         lst.append([a,b])
# lst.sort(key=lambda x: (x[1], x[0]))
# # 제일 빨리 끝나는 것 선택
# cur=0
# found=True
# while found:
#     found=False
# # 빨리 끝나는 것 중에 가장 먼저 시작하는 것을 찾는다. 
#     for j in range(cur+1, len(lst)):
#         if lst[j][0]>= lst[cur][1]:
#             cur = j
#             count +=1
#             found =True
#             break
# print(count)