first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))

if first == second == third:
    print("Кол-во одинаковых чисел: ", 3)
elif first == second or second == third or first == third:
    print("Кол-во одинаковых чисел: ", 2)
else:
    print("Кол-во одинаковых чисел: ", 0)




