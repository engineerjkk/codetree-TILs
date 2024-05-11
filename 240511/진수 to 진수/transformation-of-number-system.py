import sys
input = sys.stdin.readline
a,b = map(int,input().split())
value = str(input())

def solution(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력
tmp = int(value,a)

print(solution(tmp, b))