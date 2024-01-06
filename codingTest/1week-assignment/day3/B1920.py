


n1 = int(input())
list1 = list(map(int, input().split()))

n2 = int(input())
list2 = list(map(int, input().split()))

set1 = set(list1)  # 집합으로 정렬 순서가없고 중복불가 인덱싱불가능



for num in list2:
    if num in set1:
        print('1')
    else:
        print('0')

