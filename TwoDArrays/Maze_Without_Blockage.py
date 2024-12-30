class Solution:
    def You_Reached(self, Maze, src, dest):
        directions=[[0,-1],[0,1],[-1,0],[1,0]]

        if src == dest :
            return True

        while src != dest :
            for dir in directions:
                dir_cor1,dir_cor2 = dir
                src_cor1, src_cor2 = src
                new_cor1, new_cor2 = dir_cor1 + src_cor1, dir_cor2 + src_cor2

                d1p1, d1p2 = (dest[0] - src_cor1), (dest[1] - src_cor2)
                d2p1, d2p2 = (dest[0] - new_cor1), (dest[1] - new_cor2)

                d1 = ( d1p1*d1p1 ) + ( d1p2*d1p2 ) #dist betwn current src and dest
                d2 = ( d2p1*d2p1 ) + ( d2p2*d2p2 ) #dist betwn newCord and dest

                if d2 < d1 : 
                    src = [new_cor1, new_cor2]
                    print(src)

                if src == dest:
                    if (src[0] < len(Maze) and src[1] < len(Maze[0])) and (src[0] > -1 and src[1] > -1):
                        return 'Recehed...'
                        
                    return 'out of maze'
            
        return 'Can\'t Recehed...'

Maze=[ [0]*5 for i in range (8)]
print(Maze)
print(Solution().You_Reached(Maze, [5,1], [7,9]))
                

