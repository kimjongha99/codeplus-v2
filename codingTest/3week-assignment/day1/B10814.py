#https://www.acmicpc.net/problem/10814
#나이순 정렬


class Person:
    def __init__(self, age, name, count):
        self.age = age
        self.name = name
        self.count = count

N = int(input())
people = []

for i in range(N):
    age, name = input().split()
    age = int(age)
    people.append(Person(age, name, i))

# Sorting the people list
people.sort(key=lambda person: (person.age, person.count))

for person in people:
    print(person.age, person.name)


