eq = input().strip()

# Разбиваем строку на символы
a, op, b, eq_sign, c = eq[0], eq[1], eq[2], eq[3], eq[4]

# Определяем позицию x
if a == 'x':
    num1 = None
    num2 = int(b)
    num3 = int(c)
elif b == 'x':
    num1 = int(a)
    num2 = None
    num3 = int(c)
else:  # c == 'x'
    num1 = int(a)
    num2 = int(b)
    num3 = None

if op == '+':
    if a == 'x':
        x = num3 - num2
    elif b == 'x':
        x = num3 - num1
    else:  # c == 'x'
        x = num1 + num2
elif op == '-':
    if a == 'x':
        x = num3 + num2
    elif b == 'x':
        x = num1 - num3
    else:  # c == 'x'
        x = num1 - num2
