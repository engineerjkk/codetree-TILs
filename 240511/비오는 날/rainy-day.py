import sys
input = sys.stdin.readline
n=int(input())
lst=[]
for _ in range(n):
    lst.append(list(map(str,input().split())))

tmp=sorted(lst)
for i in tmp:
    if i[2]=='Rain':
        string=''
        for j in i:
            string+=j
            string+=' '
        print(string)
        exit()