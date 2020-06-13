a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = input("Введите знак +, -, *, /: ")

def calcul():
    if c == '+':print(a+b)

    elif c == '-':
        print(a-b)

    elif c == '*':
        print(a*b)

    elif c == '/':
        try:
            s = a / b
        except ZeroDivisionError:
            s = 0
            print(s)
        else:
            print(a/b)

