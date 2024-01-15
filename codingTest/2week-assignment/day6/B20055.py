# https://www.acmicpc.net/problem/20055
# 컨베이어벨트


N, K = map(int, input().split())  # N과 K 값을 입력받음
belt = list(map(int, input().split()))  # 컨베이어 벨트의 내구도를 입력받아 리스트에 저장
robot = [False] * N  # 로봇의 위치를 나타내는 리스트 초기화

level = 0  # 현재 레벨(단계)을 나타내는 변수 초기화

while True: # 반복문 시작
    level += 1
    tmp = belt[-1]
    for i in range(N*2-1, 0, -1): # 벨트를 한 칸씩 회전시킴
        belt[i] = belt[i-1]
    belt[0] = tmp
    print("belt:", belt)  # 현재 벨트의 상태 출력

    for i in range(N-1, 0, -1):  # 로봇을 한 칸씩 이동시킴
        robot[i] = robot[i-1]
    robot[0] = False  # 첫 번째 위치의 로봇을 False로 설정

    robot[N-1] = False  # 마지막 위치의 로봇을 내림

    for i in range(N-1, 0, -1):  # 로봇이 이동할 수 있는지 확인하고 이동시킴
        if robot[i-1] and not robot[i] and belt[i] > 0:
            robot[i-1] = False
            robot[i] = True
            belt[i] -= 1  # 이동한 위치의 내구도를 1 감소


    robot[N-1] = False

    if belt[0] > 0:
        robot[0] = True
        belt[0] -= 1

    cnt = sum(1 for x in belt if x == 0)
    if cnt >= K:
        break

print(level)
