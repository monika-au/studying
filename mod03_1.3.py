import math

v1 = int(input("Give first integer: "))
v2 = int(input("Give second integer: "))

a = max(v1, v2)
b = min(v1, v2)

if a % b == 0:
    print("Greatest common divisor is equal to ", end='')
    print(b)
    exit()
else:
    while a % b != 0:
        a_old = a
        a = b
        b = a_old % b
    print("Greatest common divisor is equal to ", end='')
    print(b)
    exit()