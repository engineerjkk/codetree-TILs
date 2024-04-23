import sys
input = sys.stdin.readline

n,m = map(int,input().split())
space=[]
for _ in range(n):
    space.append(list(map(int,input().split())))

def get_num_of_gold(space,row,col,k):
    nm=0
    for i in range(n):
        for j in range(n):
            if abs(row-i)+abs(col-j)<=k:
                nm+=space[i][j]
    return nm
answer=0
for row in range(n):
    for col in range(n):
        for k in range(n+1):
            price = get_num_of_gold(space,row,col,k)
            if price*m>=(k*k+(k+1)*(k+1)):
                answer=max(answer,price)
print(answer)