#https://www.acmicpc.net/problem/1946
#신입 사원

import sys
input = sys.stdin.readline

t = int(input())  # 테스트케이스 수
for _ in range(t):
    n = int(input())  # 지원자 수
    ranks = [list(map(int, input().split())) for _ in range(n)]  # 성적 순위
    # 서류 성적 순위로 정렬
    ranks.sort()

    # 서류, 면접 모두 합쳐 자신보다 나은 사람이 있다면 불합격
    count = 1
    interview_rank = ranks[0][1]
    # 서류 2위부터 1위와 면접 순위 비교
    for i in range(1, n):
        # 본인 면접 순위가 서류 앞 순위 사람들보다 낫다면 합격
        if ranks[i][1] < interview_rank:
            interview_rank = ranks[i][1]
            count += 1

    print(count)