from functools import reduce

#value to first factors
def func(val):
    list = []
    start=val
    for i in range(2, val + 1):
        if (val % i == 0):
            list.append(i)
            val = val / i
            next
    list.append(start)
    print(list)
    return(list)



#greatest common divisor and smallest common multiple
def calc(val1,val2):
    list1 = []
    list2 = []
    start1 = val1
    start2 = val2
    for i in range(2, val1 + 1):
        if (val1 % i == 0):
            list1.append(i)
            val1 = val1 / i
            next
    list1.append(start1)

    for i in range(2, val2 + 1):
        if (val2 % i == 0):
            list2.append(i)
            val2 = val2 / i
            next
    list2.append(start2)

    new2 = list(set(list2)-set(list1))
    deleted = list(set(list1).intersection(list2))
    gcd = reduce((lambda x, y: x*y),deleted)
    scm = reduce((lambda x, y: x*y),new2) * list1[0]
    print(gcd)
    print(scm)

int1 = int(input("Write first integer: "))
#list1 = func(int1)
int2 = int(input("Write second integer: "))
#list2 = func(int2)

calc(int1, int2)

