from collections import deque


def solution(nums, k):
    #리스트를 :3 까지 자른다.
    first_part= nums[:k]
    second_part = nums[k:]

    # 뒤에 그걸 붙힌다

    answer =  second_part+first_part

    return answer


print(solution([3, 7, 1, 5, 9, 2, 8], 3))
print(solution([2, 12, 2, 1, 3, 3, 9], 2))
print(solution([1, 2, 5, 4, 6, 7, 9], 6))
print(solution([1, 3, 6, 8, 14, 2, 1, 7], 5))


