from typing import List


def arrayPairSum( nums: List[int]) -> int:
    a = sorted(nums)   # nums 배열을 오름차순으로 정렬합니다.

    sum_of_min = 0 # 최소값들의 합을 저장할 변수를 초기화합니다.

    for i in range(0, len(a), 2):  # 정렬된 배열을 2칸씩 건너뛰며 반복합니다.
        sum_of_min += a[i] # 짝수 인덱스(0, 2, 4, ...)에 있는 요소를 합산합니다.

    print(sum_of_min)
    return sum_of_min





if __name__ == '__main__':
    assert arrayPairSum([6,2,6,5,1,2])


# 리스트를 우선 정렬하고  짝수를 더하면 결과값이 도출된다고 생각했음.