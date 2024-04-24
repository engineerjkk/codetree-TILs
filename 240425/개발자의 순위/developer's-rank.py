import sys
input = sys.stdin.readline

k,n = map(int,input().split())
lst=[]
for _ in range(k):
    lst.append(list(map(int,input().split())))
ans=0
for i in range(1,n+1):
    for j in range(1, n+1):
        if i==j:
            continue
        correct = True

        for ls in lst:
            index_i=ls.index(i)
            index_j=ls.index(j)
            if index_i>index_j:
                correct=False
        if correct:
            ans+=1
print(ans)

# arr=[[] for _ in range(21)]

# for i in range(k):
#     for j in range(n):
#         for l in range(n):
#             if i==l: 
#                 continue
#             elif lst[i][j]>lst[i][l]:
#                 arr[j+1].append(lst[i][l])
# print(arr)
# cnt=0
# for i in range(n+1):
#     for j in range(n+1):
#         if i==j:
#             continue
#         if arr[i+1].count(j)==k:
#             cnt+=1
# print(cnt)