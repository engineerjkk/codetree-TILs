# [최고의 13위치 2 ](https://www.codetree.ai/missions/18/problems/best-place-of-13-2)
해설 코드
# 변수 선언 및 입력
n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

# Step 1.
# 첫 번째 격자를 놓습니다. (i , j)
max_cnt = 0
for i in range(n):
    # 격자를 벗어나지 않을 범위로만 잡습니다.
    for j in range(n - 2):
        # 두 번째 격자를 놓습니다. (k , l)
        for k in range(n):
            # 격자를 벗어나지 않을 범위로만 잡습니다.
            for l in range(n - 2):
                # Step2. 두 격자가 겹치는 경우에는 가짓수로 세지 않습니다.
                if i == k and abs(j - l) <= 2:
                        continue
                
                # Step 3. 두 격자가 겹치지 않는 경우에 대해 동전 수를 세어 갱신해줍니다.
                cnt1 = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
                cnt2 = arr[k][l] + arr[k][l + 1] + arr[k][l + 2]
                max_cnt = max(max_cnt, cnt1 + cnt2)

print(max_cnt)
|유형|문제 경험치|난이도|
|---|---|---|
|[SK / 완전탐색 / 자리 수 단위로 완전탐색](https://www.codetree.ai/missions?missionId=18)|40xp|![보통][medium]|








[b5]: https://img.shields.io/badge/Bronze_5-%235D3E31.svg
[b4]: https://img.shields.io/badge/Bronze_4-%235D3E31.svg
[b3]: https://img.shields.io/badge/Bronze_3-%235D3E31.svg
[b2]: https://img.shields.io/badge/Bronze_2-%235D3E31.svg
[b1]: https://img.shields.io/badge/Bronze_1-%235D3E31.svg
[s5]: https://img.shields.io/badge/Silver_5-%23394960.svg
[s4]: https://img.shields.io/badge/Silver_4-%23394960.svg
[s3]: https://img.shields.io/badge/Silver_3-%23394960.svg
[s2]: https://img.shields.io/badge/Silver_2-%23394960.svg
[s1]: https://img.shields.io/badge/Silver_1-%23394960.svg
[g5]: https://img.shields.io/badge/Gold_5-%23FFC433.svg
[g4]: https://img.shields.io/badge/Gold_4-%23FFC433.svg
[g3]: https://img.shields.io/badge/Gold_3-%23FFC433.svg
[g2]: https://img.shields.io/badge/Gold_2-%23FFC433.svg
[g1]: https://img.shields.io/badge/Gold_1-%23FFC433.svg
[p5]: https://img.shields.io/badge/Platinum_5-%2376DDD8.svg
[p4]: https://img.shields.io/badge/Platinum_4-%2376DDD8.svg
[p3]: https://img.shields.io/badge/Platinum_3-%2376DDD8.svg
[p2]: https://img.shields.io/badge/Platinum_2-%2376DDD8.svg
[p1]: https://img.shields.io/badge/Platinum_1-%2376DDD8.svg
[passed]: https://img.shields.io/badge/Passed-%23009D27.svg
[failed]: https://img.shields.io/badge/Failed-%23D24D57.svg
[easy]: https://img.shields.io/badge/쉬움-%235cb85c.svg?for-the-badge
[medium]: https://img.shields.io/badge/보통-%23FFC433.svg?for-the-badge
[hard]: https://img.shields.io/badge/어려움-%23D24D57.svg?for-the-badge
