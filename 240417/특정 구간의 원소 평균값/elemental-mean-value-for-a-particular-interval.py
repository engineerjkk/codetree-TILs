import sys
input = sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))

cnt=0
for i in range(n):
    for j in range(i,n):
        tmp=[]
        for k in range(i,j+1):
           tmp.append(arr[k])
        value=sum(tmp)/len(tmp)
        if value in tmp:
            cnt+=1
print(cnt)