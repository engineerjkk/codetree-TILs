import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n, k = map(int, input().split())
lst = [int(input()) for _ in range(n)]

# 번호별로 위치를 저장할 딕셔너리
positions = defaultdict(deque)
max_number = -1

for i in range(n):
    number = lst[i]
    
    # 현재 번호가 K 거리 이내에 있는지 확인
    while positions[number] and i - positions[number][0] > k:
        positions[number].popleft()
    
    if positions[number]:
        max_number = max(max_number, number)
    
    positions[number].append(i)

print(max_number if max_number != -1 else -1)