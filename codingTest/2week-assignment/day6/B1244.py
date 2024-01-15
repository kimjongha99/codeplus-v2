# https://www.acmicpc.net/problem/1244
# 스위치 켜고 끄기

# 1부터 연속척으로 번호가 붙어있는 스위치
# 스위치는 1 <ㅡ켜져있음 0 <-꺼져있음
# 그리고 학생을 몇명 뽑음
# 학생은 자신의 성별과 ㅂ스위치번호를 받은수에따라 스위치를 조작하게됌
# 남자 -> 스위치번호가 자기가 받은수의 배수이면 그 스위치를 반대로 조작하게됌
# 여자-> 자기가 받은 수와 같은번호의 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서 그구간을 모두바꿈
# 스위치 개수는 항상 홀수


def changeArr(arr, x, y):
    if x == 1:
        if arr[y] == 0:
            return arr[y] == 1
        else:
            return arr[y] == 0


n = int(input())

arr = []

arr += map(int, input().split())

stu = int(input())

for i in range(stu):
    x, y = map(int, input().split())
    changeArr(arr, x, y)

    
for i in arr:
    print(i, end=' ')
