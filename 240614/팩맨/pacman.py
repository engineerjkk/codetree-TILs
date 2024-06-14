import sys
input = sys.stdin.readline
from itertools import product
from collections import deque
import copy
direction=[0,1,2,3]
nCr=list(product(direction,repeat=3))
nCr.sort()
dr=[-1,0,1,0]
dc=[0,-1,0,1]
dr2=[-1,-1,0,1,1,1,0,-1]
dc2=[0,-1,-1,-1,0,1,1,1]

space=[[[] for _ in range(4)] for _ in range(4)]

m,t=map(int,input().split())

class Packman:
    def __init__(self,r,c,d=0):
        self.r=r
        self.c=c
        self.d=d




r,c=map(int,input().split())
packman=Packman(r-1,c-1)
space[r-1][c-1].append(-1)

class Monster:
    def __init__(self,id,r,c,d,turn=0):
        self.id=id
        self.r=r
        self.c=c
        self.d=d
        self.turn=turn

    def get_next(self):
        return self.r+dr[self.d],self.c+dc[self.d]
    
    def change_dir(self):
        self.d=(self.d+1)%8

monsters={}
for i in range(m):
    r,c,d=map(int,input().split())
    monsters[i]=(Monster(i,r-1,c-1,d))
    space[r-1][c-1].append(i)

def duplicate_monsters():
    duplicated_mons=[]
    for key,monster2 in monsters.items():
        for monster in moster2:
            space[monster.r][monster.c].append(monster.id)
            duplicated.append(monster.id)
    for monster_id in duplicated_mons:
        mon=monsters[monster_id]
        if mon.id in mosters:
            mosters[mon.id].append(Monster(mon.id,mon.r,mon.c,mon.d,2))

def in_range(r,c):
    return -1<r<4 and -1<c<4

def check_dead(r,c):
    if -2 in space[r][c]:
        return False
    else:
        return True

def move_mosters():
    for key,monster in monster_dic.items():
        nr,nc=monster.get_next()
        if in_range(nr,nc) and check_dead(nr,nc) and (packma.r,packman.c)!=(nr,nc):
            monster.r,monster.c=nr,nc
        else:
            for i in range(8):
                monster.change_dir()
                nr,nc=monstaer.get_next()
                if in_range(nr,nc) and check_dead(nr,nc) and (packma.r,packman.c)!=(nr,nc):
                    monster.r,monster.c=nr,nc
                    break

def check_eat_monster(r,c):
    check_num=0
    if space[r][c]:
        for check_mon in space[r][c]:
            if check_mon>=0:
                check_num+=1
    return check_num

def real_eat_monster(r,c):
    if space[r][c]:
        for i in range(len(space[r][c])):
            if space[r][c][i]>=0:

                


def move_packman():
    MAX=0
    for x in nCr:
        copy_packman=copy.deepcopy(packman)
        num=0
        for i in x:
            copy_packman.d=i
            nr=copy_packman.r+dr[copy_packman.d]
            nc=copy_packman.r+dc[copy_packman.d]
            if in_range(nr,nc):
                copy_packman.r=nr
                copy_packman.c=nc
                num+=check_eat_monster(copy_packman.r,copy_packman.c)
            else:
                break
        if MAX<num:
            MAX=num
            MAX_x=x
    for i in MAX_x:
        packman.d=i
        real_eat_monster(packman.r,packman.c,packman.d)






        
def simulate():
    duplicate_monsters()
    move_mosters()
    move_packman()
    remove_dead_packman()
    success_duplicate_monster()

for _ in range(k):
    simulate()

ans=0
for i in range(4):
    for j in range(4):
        for live_moster in space[i][j]:
            if live_monster==1:
                ans+=1
print(ans)