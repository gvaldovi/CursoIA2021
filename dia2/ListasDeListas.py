
lista = [1,4,[4,5],(6,7,8),{"nombre":'Juan'}]
print(lista[-1])

#4x3
l1 = [[1,2,3],[4,5,6],[7,8,9],[0,1,2]]
print(l1)
print(l1[0][1])

#5x3x2
l2 = [[[10,2],[20,3],[40,5]],
    [[6,2],[2,30],[4,5]],
    [[7,2],[2,3],[4,5]],
    [[8,2],[2,3],[4,5]],
    [[9,2],[2,3],[4,5]]
    ]
print(l2[2][1][1])
print(l2[1][0][0])
print(l2[1][1][1])

for x in range(5):
    print(l2[x][0][0])

for y in range(3):
    print(l2[0][y][0])
print()
print(l2[0][0])
for z in range(2):
    print(l2[0][0][z])


for x in range(5):
    for y in range(3):
        for z in range(2):
            print(l2[x][y][z], end=' ')
        print()
    print()

for y in range(3):
    for z in range(2):
        for x in range(5):
            print(l2[x][y][z], end=' ')
        print()
    print()

for z in range(2):
    for x in range(5):
        for y in range(3):
            print(l2[x][y][z], end=' ')
        print()
    print()