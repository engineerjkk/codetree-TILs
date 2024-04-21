import sys
input = sys.stdin.readline

n,m = map(int,input().split())

space=[]
for _ in range(n):
    space.append(list(map(int,input().split())))

cnt=0


for i in range(n):
    tmp_row=[]
    tmp_col=[]
    for j in range(n):
        tmp_row.append(space[i][j])   
        tmp_col.append(space[j][i]) 
    real_tmp_row=[]
    real_tmp_col=[]
    for row in range(len(tmp_row)-m):
        for k in range(row,row+m):
            real_tmp_row.append(tmp_row[k])
            real_tmp_col.append(tmp_col[k])
    if len(list(set(real_tmp_row)))==1:
        cnt+=1
    if len(list(set(real_tmp_col)))==m:
        cnt+=1
print(cnt)