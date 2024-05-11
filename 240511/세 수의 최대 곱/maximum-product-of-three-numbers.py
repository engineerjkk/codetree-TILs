import sys
input = sys.stdin.readline
n = int(input())
lst=list(map(int,input().split()))
ans=-sys.maxsize

tmp=sorted(lst)

check=True
for i in tmp:
    if i<0:
        check=False

if check == True:
    ans=tmp[-1]*tmp[-2]*tmp[-3]
elif check==False:
    ans=tmp[0]*tmp[1]*tmp[-1]
    if 0 in tmp:
        ans=max(ans,0)
print(ans)