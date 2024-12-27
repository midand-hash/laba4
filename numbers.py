try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    num3 = float(input("Введите третье число: "))
    num4 = float(input("Введите четвертое число: "))
except ValueError:
    print("Ошибка: Пожалуйста, введите числовые значения.")
    exit()

sum1 = num1 + num2

sum2 = num3 + num4

if sum2 == 0:
    print("Ошибка: Вторая сумма равна нулю, деление невозможно.")
    exit()


result = sum1 / sum2

print(f"Результат: {result:.2f}")
