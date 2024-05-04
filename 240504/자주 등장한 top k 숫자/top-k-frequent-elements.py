import sys
input = sys.stdin.readline
n, k = map(int,input().split())
lst = list(map(int,input().split()))

count={}
for i in lst:
    if i in count:
        count[i]+=1
    else:
        count[i]=1

new_arr=[]
for key,value in count.items():
    new_arr.append([value,key])

new_arr = sorted(new_arr,reverse=True)
leng=len(new_arr)
for i in range(k):
    print(new_arr[i][1], end=" ")