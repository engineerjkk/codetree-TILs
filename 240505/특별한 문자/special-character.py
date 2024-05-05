import sys
input = sys.stdin.readline
lst=list(map(str,input().strip()))
dic={}
for i in lst:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1

for elem in lst:
    if dic[elem]==1:
        print(elem)
        exit()
print("None")
# sorted_dic=sorted(dic.items(),key=lambda x:x[1])
# if sorted_dic[0][1]!=1:
#     print("None")
# else:
#     for i in lst:
#         for key,value in sorted_dic:
#             if key==i and value==1:
#                 print(key)
#                 exit()