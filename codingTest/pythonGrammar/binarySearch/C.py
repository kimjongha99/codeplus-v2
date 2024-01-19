#이진 검색


def binary_search(nums, target):
    def bs(start,end):  # bs란 함수를 지정해서 어디서부터 어디까지 탐색할지 정의해주고
        if start>end:
            return  -1  #어쨋든 재귀적으로 탐색을하니 종료조건을 선언해준다.  이코드는 즉 시작점이 끝점보다 크면 말이안되니 리턴을날린다

        mid = (start + end)# 중간 지점으로 찾는 코드


        if nums[mid]>target:
            return  bs(start,mid-1)
        elif nums[mid]<target:
            return bs(mid+1,end)
        else:
            return mid

    return bs(0, len(nums) - 1)


assert binary_search(nums=[-1, 0, 3, 5, 9, 12], target=9) == 4
assert binary_search(nums=[-1, 0, 3, 5, 9, 12], target=2) == -1