from collections import deque
from sys import stdin

input= stdin.readline


tc = int(input())

for _ in range(tc):
    N, M =  map(int, input().split())
    importance = list(map(int, input().split()))
    i_deque = deque(importance)  # 큐로 만든다
    count =0 # 몇번째에 나갔는지 카운트

    while True:
        best = max(i_deque)  # 큐에서 가장 큰값
        currentOut = i_deque.popleft() # 일단 현재 큐의 제일 앞을 뽑음
        M -= 1

        if currentOut==best:
            count+=1
            if M < 0:
                print(count)
                break
        else: #뽑은 숫자가 더작다면
            i_deque.append(currentOut)
            if M<0:
                M = len(i_deque) - 1  #덱에 마지막 숫자로 대입

    M-=1







