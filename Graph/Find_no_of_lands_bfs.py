def Lands(grid):
    visited = set()
    count = 0
    for r in range (len(grid)):
        for c in range (len(grid[0])):
            if exploreNode(grid, r, c, visited):
                count  += 1


    return count

def exploreNode(grid, r, c, visited):
    if ( r < 0 or r >= len(grid)) or ( c < 0 or c >= len(grid[0])):
        return False

    if ( grid[r][c] == 'W'):
        return False
    
    cell = str(r) + ',' + str(c)
    if cell in visited:
        return False

    visited.add(cell)

    exploreNode(grid, r-1, c, visited)
    exploreNode(grid, r, c-1, visited)
    exploreNode(grid, r+1, c, visited)
    exploreNode(grid, r, c+1, visited)

    return True

grid = [['W','L','W','L'],
        ['L','L','W','L'],
        ['W','L','W','W'],
        ['L','L','W','W'],
        ['L','L','W','L']]

print(Lands(grid))

grid = [['L','L','L','L'],
        ['L','W','W','L'],
        ['L','W','W','L'],
        ['L','W','W','L'],
        ['L','L','L','L']]
    
print(Lands(grid))