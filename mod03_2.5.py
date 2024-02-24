mat = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
print(mat)

size = int(input("Integer of size of a matrix: "))
row = []
for i in range(0,size):
    if i==0:
        row.append(1)
    else:
        row.append(0)

mat=[]
for i in range(0,size):
    mat.append(row)
    row = [row[-1]] + row[:-1]

print(mat)