import sys
input = sys.stdin.readline
n=int(input())
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))


MAX=100
ans=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            overlap=False
            arr=[0]*(MAX+1)
            for x in range(n):
                if x==i or x==j or x==k:
                    continue
                for y in range(lst[x][0],lst[x][1]+1):
                    arr[y]+=1
            for x in range(MAX+1):
                if arr[x]>1:
                    overlap=True
            if overlap==False:
                ans+=1
print(ans)