def generate_passwords(L, chars):
    vowels = {'a', 'e', 'i', 'o', 'u'}  # 모음들 배열에 저장
    passwords = [] # 결과를 리스트에 담고

    def dfs(password, index):  # password는 조합들 저장 , index는 문자의 위치입니다
        if len(password) == L:
            num_vowels = sum(ch in vowels for ch in password)  #여기서 부터 이해할수없어
            num_consonants = L - num_vowels
            if num_vowels >= 1 and num_consonants >= 2:
                passwords.append(''.join(password))
            return

        for i in range(index, len(chars)):
            dfs(password + [chars[i]], i + 1)

    dfs([], 0)
    return passwords

# Input part
L, C = map(int, input().split()) #4 6
chars = input().split() #a t c i s w
chars.sort()  # a c i s t w

# Password creation
possible_passwords = generate_passwords(L, chars) #L은 문자개수 , chars는 조합할 문자들
for password in possible_passwords:
    print(password)
