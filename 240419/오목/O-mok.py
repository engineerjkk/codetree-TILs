import sys 
input = sys.stdin.readline
space=[]
for _ in range(19):
    space.append(list(map(int,input().split())))

tmp=False
for i in range(19):
    for j in range(14):
            if (space[i][j] ==1 and space[i][j+1] ==1 and space[i][j+2] ==1 and space[i][j+3] ==1 and space[i][j+4]==1):
                print(1)
                print(i+1, end=" ")
                print(j+2+1, end=" ")
                tmp=True
            if (space[i][j] ==2 and space[i][j+1]==2 and space[i][j+2]==2 and space[i][j+3]==2 and space[i][j+4]==2):
                print(2)
                print(i+1, end=" ")
                print(j+2+1, end=" ")
                tmp=True
for i in range(14):
    for j in range(19):            
            if (space[i][j] ==1 and space[i+1][j]==1 and space[i+2][j]==1 and space[i+3][j]==1 and space[i+4][j]==1):
                print(1)
                print(i+2+1, end=" ")
                print(j+1, end=" ")
                tmp=True
            elif (space[i][j] ==2 and space[i+1][j]==2 and space[i+2][j]==2 and space[i+3][j]==2 and space[i+4][j]==2):
                print(2)
                print(i+2+1, end=" ")
                print(j+1, end=" ")
                tmp=True
for i in range(14):
    for j in range(14):
            if (space[i][j] ==1 and space[i+1][j+1] ==1 and space[i+2][j+2] ==1 and space[i+3][j+3] ==1 and space[i+4][j+4]==1):
                print(1)
                print(i+2+1, end=" ")
                print(j+2+1, end=" ")
                tmp=True
            if (space[i][j] ==2 and space[i+1][j+1]==2 and space[i+2][j+2]==2 and space[i+3][j+3]==2 and space[i+4][j+4]==2):
                print(2)
                print(i+2+1, end=" ")
                print(j+2+1, end=" ")
                tmp=True

for i in range(4,19):
    for j in range(4,19):
            if (space[i][j] ==1 and space[i+1][j-1] ==1 and space[i+2][j-2] ==1 and space[i+3][j-3] ==1 and space[i+4][j-4]==1):
                print(1)
                print(i+2+1, end=" ")
                print(j-2+1, end=" ")
                tmp=True
            if (space[i][j] ==2 and space[i+1][j-1]==2 and space[i+2][j-2]==2 and space[i+3][j-3]==2 and space[i+4][j-4]==2):
                print(2)
                print(i+2+1, end=" ")
                print(j-2+1, end=" ")
                tmp=True

if tmp==False:
    print(0)