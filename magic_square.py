n = int(input("Please enter an odd number:"))
m = n // 2

lst = [[i for i in range((j - 1) * n + 1, j * n + 1)] for j in range(1, n + 1)]
target =[[0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        print(lst[i][j], end=' ')
    print()

for x in range(n):
    for y in range(n):
        if x + y < m:
            target[x + y + m + 1][m - (y - x)] = lst[x][y]
        elif x + y > 3 * m:
            target[x + y - 3 * m - 1][m - (y - x)] = lst[x][y]
        elif y < x - m:
            target[y + x - m][-m - 1 - (y - x)] = lst[x][y]
        elif y > x + m:
            target[y + x - m][3 * m + 1 - (y - x)] = lst[x][y]
        else:
            target[(x + y) - m][m - (y - x)] = lst[x][y]
            continue

print()

for i in range(n):
    for j in range(n):
        print(target[i][j], end=' ')
    print()