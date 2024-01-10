#피보나치 수열  n-1 항과 n-2 항을 더함


n = int(input())


def fibonacci(n):
    if n ==1 or n ==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


print(fibonacci(n))