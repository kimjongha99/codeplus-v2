def cal_time(h, m, needM):
    total_minutes = h * 60 + m
    total_need = total_minutes + needM

    end_hour = total_need // 60 % 24
    end_minute = total_need % 60
    return end_hour, end_minute

h, m = map(int, input().split())
needM = int(input())

end_hour, end_minute = cal_time(h, m, needM)
print(end_hour, end_minute)