from collections import deque

def rotate(arr):
    return [list(matrix[::-1]) for matrix in zip(*arr)]

k, m = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(5)]
wall_nums = deque(list(map(int, input().split())))
direc = [(-1, 0), (0, 1), (1, 0), (0, -1)]

time = 0
tmp = 0
while time < k:
    candits = []

    for i in range(1, 4):
        for j in range(1, 4):
            for rot in range(4):
                sub_arr = [arr[j-1:j+2] for arr in field[i-1:i+2]]
                sub_arr = rotate(sub_arr)

                for p in range(3):
                    for q in range(3):
                        field[p+i-1][q+j-1] = sub_arr[p][q]

                if rot == 3:
                    continue

                cur_paths = []
                visit = [[False]*5 for _ in range(5)]
                for p in range(5):
                    for q in range(5):
                        if visit[p][q]:
                            continue
                        
                        path = [(p, q)]
                        dq = deque([(p, q)])
                        visit[p][q] = True

                        while dq:
                            cx, cy = dq.popleft()                            
                            for dx, dy in direc:
                                nx, ny = cx+dx, cy+dy
                                if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                                    continue
                                if visit[nx][ny] or field[nx][ny] != field[p][q]:
                                    continue
                                visit[nx][ny] = True
                                path.append((nx, ny))
                                dq.append((nx, ny))

                        if len(path) < 3:
                            continue
                        cur_paths.extend(path)
                candits.append((cur_paths, i, j, rot)) # path, cx, cy, rot

    # select 
    candits.sort(key=lambda x: (-len(x[0]), x[3], x[2], x[1]))
    paths, cx, cy, rot = candits[0]
    if len(paths) == 0:
        break

    tmp += len(paths)

    # update
    for _ in range(rot+1):
        sub_arr = [arr[cy-1:cy+2] for arr in field[cx-1:cx+2]]
        sub_arr = rotate(sub_arr)

        for p in range(3):
            for q in range(3):
                field[p+cx-1][q+cy-1] = sub_arr[p][q]
    
    paths.sort(key=lambda x: (x[1], -x[0]))
    for tx, ty in paths:
        field[tx][ty] = wall_nums.popleft()

    # check
    while True:
        n_paths = []
        visit = [[False]*5 for _ in range(5)]
        for p in range(5):
            for q in range(5):
                if visit[p][q]:
                    continue

                paths = [(p, q)]
                dq = deque([(p, q)])
                visit[p][q] = True
                while dq:
                    cx, cy = dq.popleft()                            
                    for dx, dy in direc:
                        nx, ny = cx+dx, cy+dy
                        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                            continue
                        if visit[nx][ny] or field[nx][ny] != field[p][q]:
                            continue
                        visit[nx][ny] = True
                        paths.append((nx, ny))
                        dq.append((nx, ny))

                if len(paths) >= 3:
                    n_paths.extend(paths)

        if not n_paths:
            break

        tmp += len(n_paths)
        n_paths.sort(key=lambda x: (x[1], -x[0]))
        for tx, ty in n_paths:
            field[tx][ty] = wall_nums.popleft()

    print(tmp, end=" ")          
    tmp = 0
    time += 1