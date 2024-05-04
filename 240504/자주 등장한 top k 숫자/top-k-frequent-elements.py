n,k=map(int,input().split())
lst=list(map(int,input().split()))
dic={}
for i in lst:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
new_lst=[]
for key,value in dic.items():
    new_lst.append([value,key])
new_lst=sorted(new_lst,reverse=True)

for i in range(k):
    print(new_lst[i][1],end=" ")