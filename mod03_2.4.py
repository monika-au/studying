int1 = int(input("Integer: "))
int_start=int1
list = []

for i in range(2, int1+1):
    if(int1%i==0):
        list.append(i)
        int1=int1/i
        next

list.append(int_start)
print(list)

