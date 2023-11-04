import math

v1 = int(input("Give first integer: "))
v2 = int(input("Give second integer: "))

max_v = max(v1, v2)
min_v = min(v1, v2)

if max_v % min_v == 0:
    print("Greatest common divisor is equal to ",end='');print(min_v)
    exit()
else:
    i = math.floor(min_v/2)
    while i != 1 :
        if max_v % i == 0 and min_v % i == 0:
            print("Greatest common divisor is equal to ", end='')
            print(i)
            exit()
        i=i-1

print("Greatest common divisor is equal to 1", end='')
