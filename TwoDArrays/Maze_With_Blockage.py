def hasPath( maze: list[list[int]], start: list[int], dest: list[int]) -> bool:
    r, c = len(maze), len(maze[0])
    visited = set()

    def bfs(x, y):
        if [x,y] == dest :
            print(x,y)
            return True

        if (0 > x or x >= r) or (0 > y or y >= c):
            return False
            
        if maze[x][y] == '1':
            return False
            
        print(x,y)

        if (x,y) not in visited:
            visited.add((x,y))
        else:
            return False

        x1, y1 = x + 1, y + 0
        x2, y2 = x - 1, y + 0
        x3, y3 = x + 0, y + 1
        x4, y4 = x + 0, y - 1

        if bfs(x1, y1) or bfs(x2, y2) or bfs(x3, y3) or bfs(x4, y4):
            return True
                    
        return False

    return bfs(*start)



maze = [['0','0','0','0'],
        ['1','1','1','0'],
        ['0','0','0','0'],
        ['0','1','1','1'],
        ['0','0','0','0']]

start = [0,0]
dest = [4,3]

print(hasPath(maze, start, dest))
