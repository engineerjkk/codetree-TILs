import sys
input = sys.stdin.readline
n,m,k=map(int,input().split())
space=[]
for _ in range(n):
    space.append(list(map(int,input().split())))
next_space=[[0]*n for _ in range(n)]
traveler=[]
for _ in range(m):
    r,c=map(int,input().split())
    traveler.append([r-1,c-1])
r,c=map(int,input().split())
Exit=[r-1,c-1]
dr=[-1,0,1,0]
dc=[0,1,0,-1]
ans=0
sr,sc,square_size=0,0,0
def move_traveler():
    global Exit,ans
    for i in range(m):
        if traveler[i]==Exit:
            continue
        er,ec=Exit
        tr,tc=traveler[i]
        if er!=tr:
            nr,nc=tr,tc
            if er>tr:
                nr+=1
            else:
                nr-=1
            if space[nr][nc]==0:
                ans+=1
                traveler[i]=[nr,nc]
                continue
        if ec!=tc:
            nr,nc=tr,tc
            if ec>tc:
                nc+=1
            else:
                nc-=1
            if space[nr][nc]==0:
                ans+=1
                traveler[i]=[nr,nc]
                continue
def find_minimum_square():
    global Exit,sr,sc,square_size
    er,ec=Exit
    for size in range(2,n+1):
        for start_r in range(n-size+1):
            for start_c in range(n-size+1):
                end_r,end_c=start_r+size-1,start_c+size-1
                if not (start_r<=er<=end_r and start_c<=ec<=end_c):
                    continue
                is_in_traveler=False
                for i in range(m):
                    tr,tc=traveler[i]
                    if start_r<=tr<=end_r and start_c<=tc<=end_c:
                        if not(er==tr and ec==tc):
                            is_in_traveler=True
                if is_in_traveler:
                    sr=start_r
                    sc=start_c
                    square_size=size
                    return

def rotate_square():
    for r in range(sr,sr+square_size):
        for c in range(sc,sc+square_size):
            if space[r][c]>0:
                space[r][c]-=1
    for r in range(sr,sr+square_size):
        for c in range(sc,sc+square_size):
            Or,Oc=r-sr,c-sc
            rr,rc=Oc,square_size-Or-1
            next_space[sr+rr][sc+rc]=space[r][c]
    for r in range(sr,sr+square_size):
        for c in range(sc,sc+square_size):
            space[r][c]=next_space[r][c]           

def rotate_traveler_and_Exit():
    global Exit
    for i in range(m):
        tr,tc=traveler[i]
        if sr<=tr<sr+square_size and sc<=tc<sc+square_size:
            Or,Oc=tr-sr,tc-sc
            rr,rc=Oc,square_size-Or-1
            traveler[i]=[sr+rr,sc+rc]
    er,ec=Exit
    if sr<=er<sr+square_size and sc<=ec<sc+square_size:
        Or,Oc=er-sr,ec-sc
        rr,rc=Oc,square_size-Or-1
        Exit=[sr+rr,sc+rc]
                
        

for _ in range(k):
    move_traveler()
    is_all_escaped=True
    for i in range(m):
        if traveler[i]!=Exit:
            is_all_escaped=False
    if is_all_escaped:
        break
    find_minimum_square()
    rotate_square()
    rotate_traveler_and_Exit()
print(ans)
print(Exit[0]+1,Exit[1]+1)