n, m = map(int,input().split())
dic={}
for i in range(n):
    k=str(input())
    dic[k]=i+1
    dic[str(i+1)]=k

ans=[]
for _ in range(m):
    k=str(input())
    ans.append(dic[k])

for i in range(len(ans)):
    print(ans[i])