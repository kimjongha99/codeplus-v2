from pprint import pprint

a = list()
b= []

print(a , b ,end=' ') # 리스트 선언
print("========================")

a.append(1)
b.append(3)
print(a, b, end=' ') # append로 추가
print("========================")

a.append(2)
a.append(3)
a.insert(0,9)
print(a)  #원하는 값 삽입
print("========================")

a.append('True')
print(a) #문자열도 쉽게 삽입가능
print("========================")


#가져오기
print(a[4])
print("========================")

print(a[:5])
print("========================")


#삭제하기
a.remove(1)  # 값이 1인게 삭제됨
print(a)
print("========================")


print(a.pop(3))
print("========================")  #팝은 꺼내고 지워짐
print(a)