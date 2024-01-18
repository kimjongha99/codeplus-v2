# 학생들이 버스에 타고 여행을 가려고 합니다.
# 버스는 승객을 태울 수 있는 무게 제한이 있습니다.
# 매개변수 weight에 각 학생들의 몸무게 정보가 주어지고, limit에 버스가 태울 수 있는 총 승객
# 의 무게가 주어지면 버스에 탈 수 있는 최대인원수를 구하여 반환하는 프로그램을 작성하세
# 요.

def solution(weight, limit):
    answer = 0
    sumW = 0
    weight.sort()
    for x in weight:
        if sumW + x > limit:
            break
        sumW += x
        answer += 1

    return answer

print(solution([300, 100, 230, 120, 90, 150, 60], 700))
print(solution([50, 90, 70, 120, 300, 200, 150, 180, 190], 1000))
print(solution([70, 90, 100, 80, 60, 75, 73, 85, 120, 110, 200], 800))
print(solution([50, 90, 100, 130, 140, 120, 130, 120, 150, 160, 140, 170], 1000))
print(solution([100, 110, 50, 50, 60, 70, 50, 55, 57], 350))