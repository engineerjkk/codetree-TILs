import sys
input = sys.stdin.readline
n,m,k=map(int,input().split())
space=[[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    space[i][1:]=map(int,input().split())
next_space=[[0]*(n+1) for _ in range(n+1)]
traveler=[[-1,-1]]
for _ in range(m):
    traveler.append(list(map(int,input().split())))

exits=list(map(int,input().split()))
ans=0
sr,sc,square_size=0,0,0

def move_all_traveler():
    global exits,ans
    for i in range(1,m+1):
        if traveler[i][0]==exits[0] and traveler[i][1]==exits[1]:
            continue
        tr,tc=traveler[i]
        er,ec=exits
        if tr!=er:
            nr,nc=tr,tc
            if er>nr:
                nr+=1
            else:
                nr-=1
            if not space[nr][nc]:
                traveler[i]=[nr,nc]
                ans+=1
                continue
        if tc!=ec:
            nr,nc=tr,tc
            if ec>nc:
                nc+=1
            else:
                nc-=1
            if not space[nr][nc]:
                traveler[i]=[nr,nc]
                ans+=1
                continue

def find_minimum_square():
    global exits,sr,sc,square_size
    er,ec=exits
    for size in range(2,n+1):
        for r in range(1,n-size+2):
            for c in range(1,n-size+2):
                r2,c2=r+size-1,c+size-1
                if not (r<=er<=r2 and c<=ec<=c2):
                    continue
                is_traveler_in=False
                for i in range(1,m+1):
                    tr,tc=traveler[i]
                    if r<=tr<=r2 and c<=tc<=c2:
                        if not(tr==er and tc==ec):
                            is_traveler_in=True
                if is_traveler_in:
                    sr=r
                    sc=c
                    square_size=size
                    return
def rotate_square():
    for r in range(sr,sr+square_size):
        for c in range(sc,sc+square_size):
            if space[r][c]:
                space[r][c]-=1
    for r in range(sr,sr+square_size):
        for c in range(sc,sc+square_size):
            Or,Oc=r-sr,c-sc
            rr,rc=Oc,square_size-Or-1
            next_space[rr+sr][rc+sc]=space[r][c]
    for r in range(sr,sr+square_size):
        for c in range(sc,sc+square_size):
            space[r][c]=next_space[r][c]

def rotate_traveler_and_exit():
    global exits
    for i in range(1,m+1):
        tr,tc=traveler[i]
        if sr<=tr<sr+square_size and sc<=tc<sc+square_size:
            Or,Oc=tr-sr,tc-sc
            rr,rc=Oc,square_size-Or-1
            traveler[i]=[rr+sr,rc+sc]
    er,ec=exits
    if sr<=er<sr+square_size and sc<=ec<sc+square_size:
        Or,Oc=er-sr,ec-sc
        rr,rc=Oc,square_size-Or-1
        exits=[rr+sr,rc+sc]


for _ in range(k):
    move_all_traveler()
    is_all_escaped=True
    for i in range(1,m+1):
        if traveler[i][0]!=exits[0] or traveler[i][1]!=exits[1]:
            is_all_escaped=False
    if is_all_escaped:
        break
    find_minimum_square()
    rotate_square()
    rotate_traveler_and_exit()
print(ans)
print(exits[0],exits[1])