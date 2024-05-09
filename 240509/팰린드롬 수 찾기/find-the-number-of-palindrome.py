import sys
input = sys.stdin.readline
x,y = map(int,input().split())
cnt=0
for i in range(x,y+1):
    cha=str(i)
    cha=cha.strip()
    check=True
    for j in range(len(cha)//2):
        if cha[j]!=cha[-j-1]:
            check=False
    if check==True:
        cnt+=1
print(cnt)