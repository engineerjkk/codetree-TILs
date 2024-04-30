import sys
input = sys.stdin.readline
n= int(input())
section=[]
for _ in range(n):
    section.append(list(map(int,input().split())))
MAX_A = 100
ans=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            overlap = False
            arr=[0]*(MAX_A+1)
            for x in range(n):
                if x==i or x==j or x==k:
                    continue
                for y in range(section[x][0],section[x][1]+1):
                    arr[y]+=1
            for x in range(MAX_A+1):
                if arr[x]>1:
                    overlap=True
            if overlap==False:
                ans+=1
print(ans)