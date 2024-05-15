import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력: 
n, m = tuple(map(int, input().split()))
points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
selected_points = list()

ans = INT_MAX


def dist(p1, p2):
    (x1, y1), (x2, y2) = p1, p2
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def calc():
    # 가장 먼 거리를 반환합니다.
    return max([
        dist(p1, p2)
        for i, p1 in enumerate(selected_points)
        for j, p2 in enumerate(selected_points)
        if i != j
    ])


def find_min(idx, cnt):
    global ans
    
    if cnt == m:
        # 가장 먼 거리 중 최솟값을 선택합니다.
        ans = min(ans, calc())
        return
    
    if idx == n:
        return
    
    # 점을 선택하는 경우입니다.
    selected_points.append(points[idx])
    find_min(idx + 1, cnt + 1)
    selected_points.pop()
    
    # 점을 선택하지 않는 경우입니다.
    find_min(idx + 1, cnt)


find_min(0, 0)
print(ans)