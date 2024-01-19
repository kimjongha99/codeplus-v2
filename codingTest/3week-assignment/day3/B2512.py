# //https://www.acmicpc.net/problem/2512
# //예산


n = int(input())
arr = list(map(int,input().split()))
k = int(input())

arr.sort()

start =0
end = arr[n-1]
result =0

while start<=end:  # 시작값보다 end값이 커지면종료
    mid = (start+end)//2
    sum =0

    for i in range(n):
        if arr[i]>mid:# 예산을 초과하지않으면서 가능한 최대로 할당해야하기때문에  현재 예산 상한액보다 ar[i]가 크다면 그지방에는 mid만큼할당해야합니다
            sum += mid
        else:
            sum += arr[i] # 그게아니면 arr[i]만큼 할당


    if sum >k: #만약 총 에산액이 m보다 크다면  상한값이 너무 크다는의미로 mid에 1을 줄여서 범위를 좁히고
        end = mid-1
    else:
        start= mid+1  #예산액보다 작다면 mid의값은 더 커져도 된다는거니까 start에 mid+1을 증가해주고
        result= max(result,mid) #그 mid값은 유효값이니깐 result에 넣어줌

print(result)




