import sys
input = sys.stdin.readline

n=int(input())
lst=[]
for i in range(n):
    lst.append(list(map(str,input().strip())))

count={}
a=ord('a')
for i in lst:
    cnt=0
    for j in i:
        cnt+= (a-ord(j))
    if cnt in count:
        count[cnt]+=1
    else:
        count[cnt]=1
count2=sorted(count.items(),reverse=True)
print(count2[0][1])