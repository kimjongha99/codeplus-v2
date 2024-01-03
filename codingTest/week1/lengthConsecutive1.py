def solution(nums):
    max_length = 0  # To store the length of the longest sequence of 1s
    current_length = 0  # To store the length of the current sequence of 1s
    n = len(nums)  # Length of the list

    for i in range(n):
        if nums[i] == 1:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0  # Reset the current length if 0 is found

    return max_length


print(solution([1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1]))
print(solution([0, 0, 1, 0, 1, 0, 0]))
print(solution([1, 1, 1, 1, 1]))
print(solution([1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1]))
