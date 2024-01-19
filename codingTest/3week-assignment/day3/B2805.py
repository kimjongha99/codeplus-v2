#https://www.acmicpc.net/problem/2805
#나무자르기



n, m = map(int, input().split())
trees = list(map(int, input().split()))

max_height = max(trees)  # 최대 절단 높이
min_height = 0           # 최소 절단 높이

while min_height < max_height:
    mid_height = (max_height + min_height) // 2
    sum_of_cut = 0

    for tree in trees:
        if tree - mid_height > 0:
            sum_of_cut += tree - mid_height

    if sum_of_cut < m:
        max_height = mid_height
    else:
        min_height = mid_height + 1

print(min_height - 1)
