import sys
input = sys.stdin.readline
n,m= map(int,input().split())
space=[]
for _ in range(n):
    space.append(list(map(int,input().split())))

ans=-sys.maxsize
board=[[0]*m for _ in range(n)]

def clearboard():
    for i in range(n):
        for j in range(m):
            board[i][j]=0

def draw_rec(x1,y1,x2,y2):
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            board[i][j]+=1
def checkboard():
    for i in range(n):
        for j in range(m):
            if board[i][j]>=2:
                return False
    return True



def overlapped(x1,y1,x2,y2,x3,y3,x4,y4):
    clearboard()
    draw_rec(x1,y1,x2,y2)
    draw_rec(x3,y3,x4,y4)
    return checkboard()

def rec(x1,y1,x2,y2):
    nm=0
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            nm+=space[i][j]
    return nm


def find_max_rec(x1,y1,x2,y2):
    ans2=-sys.maxsize
    for i in range(n):
        for j in range(m):
            for k in range(i,n):
                for l in range(j,m):
                    if overlapped(i,j,k,l,x1,y1,x2,y2):
                        ans2=max(ans2,rec(i,j,k,l)+rec(x1,y1,x2,y2))
    return ans2

for i in range(n):
    for j in range(m):
        for k in range(i,n):
            for l in range(j,m):
                ans=max(ans,find_max_rec(i,j,k,l))
print(ans)