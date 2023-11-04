# values for the first line
st1 = int(input("Where first line starts?: "))
en1 = int(input("Where first line ends?: "))

#exiting program when finding errors in values
if en1 < st1:
    print("Values are not right. End value should be higher")
    exit()
elif en1 == st1:
    print("Values cannot be equal")
    exit()

# values for the second line
st2 = int(input("Where second line starts?: "))
en2 = int(input("Where second line ends?: "))

#exiting program when finding errors in values
if en2 < st2:
    print("Values are not right. End value should be higher")
    exit()
elif en2 == st2:
    print("Values cannot be equal")
    exit()

#parameters used in conditional statements
min_st = min(st1, st2)
max_st = max(st1, st2)
min_en = min(en1, en2)
max_en = max(en1, en2)
l = max_en - min_st

#comparing start and end points of lines
if st1 > en2 or st2 > en1:
    print("Lines are disconnected")
elif st1 == en2 or st2 == en1:
    print("Lines have common point, ",end=''); print("their length is", end=''); print(l)
else:
    print("Common part for lines is from ",end='');print(max_st,end='');print(" to ", end='');print(min_en)
    print("Sum length of those line is ",end='');print(l)


