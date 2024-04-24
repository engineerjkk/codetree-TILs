import sys
input= sys.stdin.readline
n=int(input())
lines=[]
for _ in range(n):
    lines.append(list(map(int,input().split())))

for i in range(n):
    cnt=0
    for j in range(n):
        overlapped=False
        if i==j:
            continue
        
        if (lines[i][0] <=lines[j][0] and lines[i][1] >=lines[j][1]) or (lines[i][0] >= lines[j][0] and lines[i][0] <= lines[j][1]):
            overlapped=True
            cnt+=1
print(cnt)