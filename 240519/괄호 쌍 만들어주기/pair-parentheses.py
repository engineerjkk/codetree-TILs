import sys
input = sys.stdin.readline

lst=input()
R=[0]*len(lst)
n=len(lst)-1
R[n]=lst[n]
cnt=0
for i in range(n-2):
    for j in range(i+2,n):
        if lst[i]+lst[i+1]=='((' and lst[j]+lst[j+1]=='))':
            cnt+=1
print(cnt)