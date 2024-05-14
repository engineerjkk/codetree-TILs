import sys
input = sys.stdin.readline
n=int(input())
start=input()
end=input()

ans=0
cnt=0
mismatched=False
for i in range(n):
    if start[i] != end[i]:
        cnt+=1
        if mismatched==False:
            ans+=1
            mismatched=True
        if cnt>4:
            cnt=0
            mismatched=False
            
    else:
        mismatched=False
        cnt=0
print(ans)