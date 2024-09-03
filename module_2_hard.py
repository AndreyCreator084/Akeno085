def get_password(number):
    password_ = ''
    for i in range(1, number):
        for j in range(2, number):
            if j <= i:
                continue
            if number % (i + j) == 0:
                password_ += str(i) + str(j)
    return password_

n = int(input('Введите число для первой ячейки от 3 до 20: '))

result_ = get_password(n)
print('Пароль от ворот:', result_)
print('Вы справились, Поздравляем! :)')