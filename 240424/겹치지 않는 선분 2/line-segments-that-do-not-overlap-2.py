import sys
input = sys.stdin.readline
n = int(input())

lines=[]
for _ in range(n):
    lines.append(list(map(int,input().split())))
ans=0

for i in range(n):
    overlap=False
    for j in range(n):
        if i==j:
            continue
        
        if (lines[i][0]<=lines[j][0] and lines[i][1] >=lines[j][1]) or (lines[i][0] >=lines[j][0] and lines[i][1]<=lines[j][1]):
            overlap = True
            break
    if overlap == False:
        ans+=1
print(ans)