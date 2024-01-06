#이문제는 아이디와 비밀번호를 입력받고 아이디를 입력하면 비밀번호 출력되게 하는문제
#https://www.acmicpc.net/problem/17219


# 입력 예시처럼 한줄에 2개의 정수를 입력받음
n, m = map(int, input().split())

id_dict = {}  #key , value를 저장하기위해서 id_dict를 초기화해줌

for _ in range(n):  # 입력의 예시대로 n번 루프 돌면서 키와 벨류 를 입력받고 id_dict 저장해줌
    key, value= input().split()
    id_dict[key]=value

for _ in range(m): # 이제 출력을 해야하니
    id = input().strip() # 찾아야하는 값을 입력받고
    if id in id_dict:  # id_dict 안에 id가 있으면
        print(id_dict[id]) #출력












# 트러블 슈팅
# 리트코드와 백준의 입출력이 달라서 사이트마다 입출력부터 고민을 해야했다..
# 개인적인 의견 백준이 좀더 잘 풀리는것같다.





#인풋
# 16 4
# noj.am IU
# acmicpc.net UAENA
# startlink.io THEKINGOD
# google.com ZEZE
# nate.com VOICEMAIL
# naver.com REDQUEEN
# daum.net MODERNTIMES
# utube.com BLACKOUT
# zum.com LASTFANTASY
# dreamwiz.com RAINDROP
# hanyang.ac.kr SOMEDAY
# dhlottery.co.kr BOO
# duksoo.hs.kr HAVANA
# hanyang-u.ms.kr OBLIVIATE
# yd.es.kr LOVEATTACK
# mcc.hanyang.ac.kr ADREAMER
# startlink.io
# acmicpc.net
# noj.am
# mcc.hanyang.ac.kr