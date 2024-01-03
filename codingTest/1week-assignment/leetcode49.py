from collections import defaultdict
from typing import List


def groupAnagrams( strs: List[str]) -> List[List[str]]:
    # 각 값이 목록으로 초기화되는 defaultdict를 만듭니다.
    anagrams = defaultdict(list)

    # 제공된 목록의 각 문자열을 반복합니다.
    for s in strs:
        key= ''.join(sorted(s))
        anagrams[key].append(s)


    print(list(anagrams.values()))
    return list(anagrams.values())


if __name__ == '__main__':
    assert groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]
)

