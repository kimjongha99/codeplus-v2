# 1. **Disjoint Set 클래스 정의**: 이는 유니온 파인드 알고리즘을 구현하여 집합들의 합집합과 대표원소를 찾는 데 사용됩니다.
# 2. **메인 함수**: 노드와 간선의 수, 그리고 연결 여부를 확인할 두 노드를 입력받습니다.
# 3. **간선 입력**: 모든 간선과 그들의 가중치를 입력받고, 가중치에 따라 내림차순으로 정렬합니다.
# 4. **크루스칼 알고리즘 실행**: 가중치가 가장 큰 간선부터 시작하여, 두 노드가 연결될 때까지 간선을 집합에 추가합니다.
# 5. **결과 출력**: 두 노드가 연결되었는지 확인하고, 연결되었다면 마지막으로 추가된 간선의 가중치를 출력합니다. 연결되지 않았다면 0을 출력합니다
#

class DisjointSet:

    def __init__(self, n):
        self.parent = list(range(n + 1))

    def find(self, x):     # find 함수: x의 루트 노드를 찾습니다. 경로 압축을 사용하여 효율성을 높입니다.

        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):     # union 함수: 두 요소를 하나의 집합으로 합칩니다.

        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        self.parent[root_x] = root_y


if __name__ == '__main__':
    from sys import stdin, setrecursionlimit
    input = stdin.readline
    setrecursionlimit(10 ** 5)

    # n: 노드의 수, m: 간선의 수
    n, m = map(int, input().split())
    # s, e: 연결 여부를 확인할 두 노드
    s, e = map(int, input().split())
    bridge = []
    for _ in range(m):
        x, y, k = map(int, input().split())
        bridge.append((k, x, y))
    bridge.sort()     # 간선들을 가중치에 따라 내림차순으로 정렬합니다.
    djs = DisjointSet(n)
    last = 0
    while djs.find(s) != djs.find(e) and bridge:     # 두 노드가 연결될 때까지 간선들을 확인합니다.
        # 현재 간선을 가져옵니다. d: 가중치, x, y: 연결된 노드
        d, x, y = bridge.pop()
        # 마지막으로 추가된 간선의 가중치를 업데이트합니다.
        last = d
        # 두 노드를 연결합니다.
        djs.union(x, y)
    print(last if djs.find(s) == djs.find(e) else 0)     # 두 노드가 연결되었는지 확인하고, 연결되었다면 마지막 간선의 가중치를, 아니라면 0을 출력합니다.
