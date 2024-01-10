# https://www.acmicpc.net/problem/2002


# 추월

#반례가 뭐지 도대체


tc = int(input())

dict_1 = {}
dict_2 = {}
for i in range(tc):
    key = input()
    dict_1[key] = i

for i in range(tc):
    key = input()
    dict_2[key] = i

count = 0

out_keys = list(dict_2.keys())

for i in range(len(out_keys)):
    now_in = dict_1[out_keys[i]]
    for j in range(i+1, len(out_keys)):
        next_in = dict_1[out_keys[j]]
        if next_in < now_in:
            count += 1
            break


print(count)
