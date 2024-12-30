def Doors()-> list[list[int]]:
    num = 1 
    opendoors = []
    closeddoors = []
    count = 1
    for i in range (1, 101):
        if i ** 0.5 == num:
            opendoors.append(i)
            num += 1
        else:
            closeddoors.append(i)

    return [opendoors, closeddoors]



answer = Doors()
print('open = ', answer[0])
print('close = ', answer[1])