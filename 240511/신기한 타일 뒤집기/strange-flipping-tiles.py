n=int(input())
lst=[]
for _ in range(n):
    lst.append(list(map(str,input().split())))

arr=[0]*1001

current=500
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