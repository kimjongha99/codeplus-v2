# 백준 10809번 알파벳 찾기
import string


def get_idx_naive(word):
    result = [-1] * len(string.ascii_lowercase)  # 알파벳의 각 문자에 대해 하나씩 -1 목록을 초기화합니다.

    for i in range(len(word)):  # 입력 단어의 각 문자를 반복합니다.
        char = word[i]  # 'char'는 'word'의 현재 문자입니다.

        for j in range(len(string.ascii_lowercase)): # 영어 소문자 알파벳의 각 문자를 반복합니다.

            lo = string.ascii_lowercase[j]; # 'lo'는 현재 알파벳의 소문자입니다.

            if result[j] == -1 and char == lo:  # 'word'에서 'lo'가 처음 나타나는지 확인합니다.
                result[j] = i # 그렇다면 'result'에서 해당 인덱스를 업데이트합니다.

    print(' '.join(map(str, result)))


get_idx_naive(input());


