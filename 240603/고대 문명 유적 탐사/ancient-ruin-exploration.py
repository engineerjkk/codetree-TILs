from collections import deque
import copy

N_large = 5  # 고대 문명 전체 격자 크기입니다.
N_small = 3  # 회전시킬 격자의 크기입니다.

# 고대 문명 격자를 정의합니다
class Board:
    def __init__(self):
        self.space = [[0 for _ in range(N_large)] for _ in range(N_large)]

    def in_range(self, y, x):
        # 주어진 y, x가 고대 문명 격자의 범위안에 있는지 확인하는 함수 입니다.
        return 0 <= y < N_large and 0 <= x < N_large

    # 현재 격자에서 sy, sx를 좌측상단으로 하여 시계방향 90도 회전을 cnt번 시행했을때 결과를 return 합니다.
    def rotate(self, r, c, cnt):
        result = Board()
        #result.a = [row[:] for row in self.a]
        result.space=copy.deepcopy(self.space)
        for _ in range(cnt):
            # sy, sx를 좌측상단으로 하여 시계방향 90도 회전합니다.
            tmp = result.space[r + 0][c + 2]
            result.space[r + 0][c + 2] = result.space[r + 0][c + 0]
            result.space[r + 0][c + 0] = result.space[r + 2][c + 0]
            result.space[r + 2][c + 0] = result.space[r + 2][c + 2]
            result.space[r + 2][c + 2] = tmp
            tmp = result.space[r + 1][c + 2]
            result.space[r + 1][c + 2] = result.space[r + 0][c + 1]
            result.space[r + 0][c + 1] = result.space[r + 1][c + 0]
            result.space[r + 1][c + 0] = result.space[r + 2][c + 1]
            result.space[r + 2][c + 1] = tmp
        return result

    # 현재 격자에서 유물을 획득합니다.
    # 새로운 유물 조각을 채우는것은 여기서 고려하지 않습니다.
    def cal_score(self):
        score = 0
        visit = [[False for _ in range(N_large)] for _ in range(N_large)]
        dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]

        for i in range(N_large):
            for j in range(N_large):
                if not visit[i][j]:
                    # BFS를 활용한 Flood Fill 알고리즘을 사용하여 visit 배열을 채웁니다.
                    # 이때 trace 안에 조각들의 위치가 저장됩니다.
                    queue=deque()
                    queue.append((i,j))
                    trace=deque()
                    trace.append((i,j))
                    visit[i][j] = True
                    while queue:
                        r,c = queue.popleft()
                        for k in range(4):
                            nr, nc = r + dr[k], c + dc[k]
                            if self.in_range(nr, nc) and self.space[nr][nc] == self.space[r][c] and not visit[nr][nc]:
                                queue.append((nr, nc))
                                trace.append((nr, nc))
                                visit[nr][nc] = True
                    # 위에서 진행된 Flood Fill을 통해 조각들이 모여 유물이 되고 사라지는지 확인힙니다.
                    if len(trace) >= 3:
                        # 유물이 되어 사라지는 경우 가치를 더해주고 조각이 비어있음을 뜻하는 0으로 바꿔줍니다.
                        score += len(trace)
                        while trace:
                            r,c = trace.popleft()
                            self.space[r][c] = 0
        return score

    # 유물 획득과정에서 조각이 비어있는 곳에 새로운 조각을 채워줍니다.
    def fill(self, queue):
        # 열이 작고 행이 큰 우선순위로 채워줍니다.
        for j in range(N_large):
            for i in reversed(range(N_large)):
                if self.space[i][j] == 0:
                    self.space[i][j] = queue.popleft()

def main():
    # 입력을 받습니다.
    K, M = map(int, input().split())
    board = Board()
    for i in range(N_large):
        board.space[i] = list(map(int, input().split()))
    queue = deque()
    for t in list(map(int, input().split())):
        queue.append(t)

    # 최대 K번의 탐사과정을 거칩니다.
    for _ in range(K):
        maxScore = 0
        maxScoreBoard = None
        # 회전 목표에 맞는 결과를 maxScoreBoard에 저장합니다.
        # (1) 유물 1차 획득 가치를 최대화
        # (2) 회전한 각도가 가장 작은 방법을 선택
        # (3) 회전 중심 좌표의 열이 가장 작은 구간을, 그리고 열이 같다면 행이 가장 작은 구간을 선택
        for cnt in range(1, 4):
            for sc in range(N_large - N_small + 1):
                for sr in range(N_large - N_small + 1):
                    rotated = board.rotate(sr, sc, cnt)
                    score = rotated.cal_score()
                    if maxScore < score:
                        maxScore = score
                        maxScoreBoard = rotated
        # 회전을 통해 더 이상 유물을 획득할 수 없는 경우 탐사를 종료합니다.
        if maxScoreBoard is None:
            break
        board = maxScoreBoard
        # 유물의 연쇄 획득을 위해 유물 조각을 채우고 유물을 획득하는 과정을 더이상 획득할 수 있는 유물이 없을때까지 반복합니다.
        while True:
            board.fill(queue)
            newScore = board.cal_score()
            if newScore == 0:
                break
            maxScore += newScore

        print(maxScore, end=" ")

if __name__ == '__main__':
    main()