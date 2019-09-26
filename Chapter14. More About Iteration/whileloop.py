def SumTo(n_num):
    sum = 0
    num = 1
    while num <= n_num:
        sum = sum + num
        num = num + 1
    return sum


print(SumTo(4))