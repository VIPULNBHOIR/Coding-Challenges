def tapwater(heights):
    n = len(heights)
    max = heights[0]
    ptr = 0
    total = 0
    trap_H20 = 0
    
    for idx in range(1,n):
        height = heights[idx]
        if height >= max:
            max = height
            ptr = idx
            trap_H20 += total
            total = 0
        else:
            total += (max - height)

    if max > heights[-1]:
        total = 0
        max = heights[-1]
        for idx in range(n-2, ptr - 1, -1):
            height = heights[idx]
            if height >= max:
                max = height
                ptr = idx
                trap_H20 += total
                total = 0
                
            else:
                total += (max - height)

    return trap_H20

print(tapwater([5,0,0,4]))