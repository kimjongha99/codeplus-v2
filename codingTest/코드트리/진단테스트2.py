

def fun1(a, b):
    sort_a =[]
    sort_b =[]

    for i in a:
        if i%2==0:
            sort_a.append(i)

    for i in b:
        if i%2 !=0:
            sort_b.append(i)

    return sorted(sort_a) + sorted(sort_b, reverse=True)


n = int(input())
a = map(int,input().split())
b = map(int,input().split())

answer = fun1(a,b)

print(answer)
