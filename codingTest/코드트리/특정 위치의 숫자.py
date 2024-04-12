#10개의 정수를 입력받습니다.
#입력받은 정수에서 세 번째, 다섯 번째, 열 번째 정수의 합을 출력하는 프로그램을 작성해보세요.


arr = list(map(int, input().split()))
print(arr[2] + arr[4] + arr[9])