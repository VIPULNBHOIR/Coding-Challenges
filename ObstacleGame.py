n = int(input())

matrix = [ list(map(str, input().split())) for _ in range(n)]
route = (0, 0)
found = 0
D = False
visited = set()

points = ((1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1))

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'A':
            visited.add((i,j))
            route = (i, j)
            found =  True
            break
    if found:
        break



while (not D):
    hurdles = []
    for point in points:
        newi, newj = route[0] + point[0], route[1] + point[1]

        if newi >=n or newi < 0 or newj >=n or newj < 0 or matrix[newi][newj] == 'M' or matrix[newi][newj] == 'A':
            pass

        elif matrix[newi][newj] == 'R' and (newi, newj) not in visited:
            newroute = newi, newj
            visited.add((newi, newj))

        elif matrix[newi][newj] == 'D':
            D = True

        else:
            if matrix[newi][newj] != 'R':
                hurdles.append(matrix[newi][newj])

    route = newroute

    hurdles.sort()
    if hurdles:
        for hurdle in hurdles:
            print(hurdle, end='')
    else:
        print('No HURDLES')
    print()

print('DESTINATION')

