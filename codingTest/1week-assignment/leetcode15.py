from typing import List

# 합이 0으로 될수있는 3개엘리먼트 출력
# 부루트 포스는 시간초과
# 따라서 투포인터로 left , right 으 간격을 좁히면서 풀이
def threeSum( nums: List[int]) -> List[List[int]]:
    result= []
    nums.sort()

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]: # 중복된 원소를 건너뛰기 위한 조건문입니다. 같은 원소가 연속해서 나오면 건너뜁니다.

            continue


        # 두 개의 포인터를 초기화합니다. 하나는 현재 원소의 다음 위치(left), 다른 하나는 배열의 끝 위치(right)에 둡니다.
        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
                # 합이 0이면 유효한 삼중항을 찾은 것이므로 결과 리스트에 추가합니다.
            else:
                result.append([nums[i], nums[left], nums[right]])
                # 중복된 값들을 건너뛰기 위해 left와 right 포인터를 조정합니다.
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                    # 새로운 삼중항을 찾기 위해 두 포인터 모두 이동시킵니다.
                left += 1
                right -= 1


    print(result)
    return result

if __name__ == '__main__':
    assert threeSum([-1,0,1,2,-1,-4])


