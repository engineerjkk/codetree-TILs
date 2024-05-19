import sys
input = sys.stdin.readline

lst=input()
R=[0]*len(lst)
n=len(lst)-1
cnt=0
for i in range(n-1,-1,-1):
    if lst[i]+lst[i+1]=='))':
        R[i]=cnt
        cnt+=1
    R[i]=cnt
ans=0    
for i in range(n-2):
    if lst[i]+lst[i+1]=='((':
        ans+=R[i]

print(ans)