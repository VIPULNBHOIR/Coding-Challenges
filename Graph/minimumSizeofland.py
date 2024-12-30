def Lands(grid):
    visited = set()
    min = float("inf")
    for r in range (len(grid)):
        for c in range (len(grid[0])):
            curr = exploreNode(grid, r, c, visited, 1) 
            if min > curr and curr != 0:
                min = curr

    return min

def exploreNode(grid, r, c, visited, cnt):
    if ( r < 0 or r >= len(grid)) or ( c < 0 or c >= len(grid[0])):
        return 0

    if ( grid[r][c] == 'W'):
        return 0
    
    cell = str(r) + ',' + str(c)
    if cell in visited:
        return 0

    visited.add(cell)


    cnt += exploreNode(grid, r-1, c, visited, cnt)
    cnt += exploreNode(grid, r, c-1, visited, cnt)
    cnt += exploreNode(grid, r+1, c, visited, cnt)
    cnt += exploreNode(grid, r, c+1, visited, cnt)

    return cnt

grid = [['W','L','W','L'],
        ['L','L','W','L'],
        ['W','L','W','W'],
        ['L','L','W','W'],
        ['L','L','W','W']]

print(Lands(grid))

grid = [['L','L','L','L'],
        ['L','W','W','L'],
        ['L','W','W','L'],
        ['L','W','W','L'],
        ['L','L','L','L']]
    
print(Lands(grid))