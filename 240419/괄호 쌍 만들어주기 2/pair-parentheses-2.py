import sys
input = sys.stdin.readline
lst=list(map(str,input().strip()))

cnt=0
for i in range(len(lst)-3):
    for j in range(i+1,len(lst)-1):
        if lst[i]=="(" and lst[i+1]=="(" and lst[j] == ")" and lst[j+1]==")":
            cnt+=1
print(cnt)