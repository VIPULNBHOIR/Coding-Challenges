def BS(cords, mid):
    cows = 1
    ptr1 = 0
    for i in range(1, Ncord):
        if cords[i] - cords[ptr1] >= mid:
            cows += 1
            ptr1 = i

    return cows

if __name__ == '__main__':

    cordinates = [8,3,5,9,15]
    cows = 5
    Ncord = 5

    # for i in range(Ncord):
    #     cordinates.append(int(input()))

    cordinates = sorted(cordinates)
    min = 1
    max = cordinates[Ncord-1] - cordinates[0]

    while min <= max:
        mid = (min + max) // 2
        res = BS(cordinates, mid)

        if res < cows:
            max = mid - 1
        else:
            min = mid + 1

    print(max)