import sys
input = sys.stdin.readline
n=int(input())
lst=[]
for _ in range(n):
    lst.append(list(map(str,input().split())))

arr=[0]*(1000*100+1)

current=(1000*100+1)//2
for i in range(n):
    cnt,direction = lst[i]
    cnt=int(cnt)
    if direction == 'R':
        arr[current]=1
        for j in range(cnt-1):
            current+=1
            arr[current]=1        
    else:
        arr[current]=-1
        for j in range(cnt-1):
            current-=1
            arr[current]=-1
print(arr.count(-1),end=" ")
print(arr.count(1))