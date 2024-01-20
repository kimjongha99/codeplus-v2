#배열로 이진트리 표현하기
# 자식 노드와 부모 노드를 찾기


tree = ["A", "B", "C", "D", "E", "F", None, "G"]


i =0
n = len(tree)

while i<n:
    print(f"Parent: {tree[i]}", end=", ")
    left = 2* i +1
    right = left +1
    if left < n and tree[left] is not None:
        print(f"Left: {tree[left]}", end=", ")
    if right < n and tree[right] is not None:
        print(f"Right: {tree[right]}", end=" ")
    print()
    i += 1