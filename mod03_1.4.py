a = 0
b = 0

while a is b:
    a = a - 1
    b = b - 1
minimum = a

a = 0
b = 0

while a is b:
    a = a + 1
    b = b + 1
maximum = b

print("Range of cached values are from ", end='')
print(minimum,end='')
print(" to ",end='')
print(maximum)
