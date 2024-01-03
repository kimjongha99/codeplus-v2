def mergeAlternately(word1: str, word2: str) -> str:
    merged_word = "" # 결과를 저장하기 위해 빈 문자열을 초기화합니다.

    max_length = max(len(word1), len(word2))
    for i in range(max_length):
        if i < len(word1):
            merged_word += word1[i]
        if i < len(word2):
            merged_word += word2[i]


    print(merged_word)
    return merged_word


if __name__ == '__main__':
    assert mergeAlternately(  "abc",  "pqr")