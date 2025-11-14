# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.linspace(-10, 10, 100)
# y = x**2
#
# plt.plot(x, y)
# plt.title('y = x²')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.grid(True)
# plt.show()

def calculator():
    print("Простой калькулятор")
    print("Доступные операции: +, -, *, /")
    print("Для выхода введите 'q'")

    while True:
        try:
            num1 = input("Введите первое число (или 'q' для выхода): ")
            if num1.lower() == 'q':
                break
            num1 = float(num1)

            operation = input("Введите операцию (+, -, *, /): ")
            if operation.lower() == 'q':
                break

            num2 = float(input("Введите второе число: "))

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    print("Ошибка: деление на ноль!")
                    continue
                result = num1 / num2
            else:
                print("Неизвестная операция!")
                continue