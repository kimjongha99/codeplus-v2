# 매개변수 box에 각 박스 종류의 정보가 주어지고, limit에 트럭의 실을 수 있는 박스의 최대
# 개수가 주어지면 트럭에 실을 수 있는 사과의 최대 개수를 반환하는 프로그램을 작성하세요


def solution(box, limit):
    answer =0;
    box.sort(key= lambda v: -v[1])# 배열의 1번 인덱스 즉 [0, 1]에서 1번 기준 내림차순정렬한것
    print(box)

    for x in box:
        cnt = min(limit,x[0])
        answer += cnt*x[1]
        limit -= cnt
        if limit == 0:
            break
    return answer


print(solution([[2, 20], [2, 10], [3, 15], [2, 30]], 5))
print(solution([[1, 50], [2, 20], [3, 30], [2, 31], [5, 25]], 10))
print(solution([[3, 40], [5, 20], [5, 70], [1, 80], [5, 30], [3, 35]], 15))
print(solution([[2, 70], [5, 100], [3, 90], [1, 95]], 8))
print(solution([[80, 20], [50, 10], [70, 15], [70, 30], [80, 70], [90, 88], [70, 75]], 500))
