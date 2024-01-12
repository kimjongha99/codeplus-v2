# nums에 오름차순으로 정렬된 정수 배열이 주어지고, target에 nums배열에서 찾고자 하는 값
# 이 주어지면 nums배열에서 target의 인덱스 번호를 찾아 반환하는 프로그램을 작성하세요.
# 인덱스 번호는 0번부터 시작합니다.
# target값이 nums에 존재하지 않을 경우 -1를 반환합니다.


def solution(nums, target):
    answer = 0
    left =0
    right =len(nums)-1
    while  left<=right:
        mid = (left+right)//2
        if target == nums[mid]:
            return mid
        if target>nums[mid]:
            left= mid+1
        else:
            right=mid-1


 
    return answer


print(solution([2, 5, 7, 8, 10, 15, 20, 24, 25, 30], 8))
print(solution([-3, 0, 2, 5, 8, 9, 12, 15], 0))
print(solution([-5, -2, -1, 3, 8, 9, 12, 17, 23], 2))
print(solution([3, 6, 9, 12, 17, 29, 33], 3))
print(solution([1, 2, 3, 4, 5, 7, 9, 11, 12, 15, 16, 17, 18], 18))
