n,m,k = map(int,input().split())
lst=[]
ans=False
for _ in range(m):
    lst.append(int(input()))
tmp=[0]*(n+1)
for i in lst:
    tmp.append(i)
for j,num in enumerate(lst):
    tmp[num]+=1
    if tmp[num]>=k:
        print(num)
        exit()
print(-1)
    
# for i in range(k):
#     for j,num in enumerate(lst):
#         tmp[num]-=1
#         if tmp[num]==0:
#             print(num)
#             exit()
# print(-1)