n= int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
D=list(map(int,input().split()))

count={}
ans=0

for i in range(n):
    for j in range(n):
        sum_val=A[i]+B[j]
        if sum_val in count:
            count[sum_val]+=1
        else:
            count[sum_val]=1
for i in range(n):
    for j in range(n):
        diff = -C[i] - D[j]
        if diff in count:
            ans += count[diff]
print(ans)