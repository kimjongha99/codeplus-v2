import sys

tc = int(sys.stdin.readline())

for _ in range(tc):
    str = input()

    left_list=[]
    right_list=[]

    for s in str:
        if s == '>':
            if right_list:
                left_list.append(right_list.pop())
        elif s == '<':
            if left_list:
                right_list.append(left_list.pop())
        elif s == '-':
            if left_list:
                left_list.pop()
        else:
            left_list.append(s)

    print(right_list)


    final_output = ''.join(left_list) + ''.join(reversed(right_list))
    print(final_output)
