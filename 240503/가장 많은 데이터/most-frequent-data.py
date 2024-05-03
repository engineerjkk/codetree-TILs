import sys
input = sys.stdin.readline

n = int(input())
dic={}
for _ in range(n):
    k=str(input())
    if k in dic:
        dic[k]+=1
    else:
        dic[k]=1
ans=0
for i in dic:
    value = dic[i]
    ans=max(ans,value)
print(ans)