def Fibbo(n: int):
    var1 = 0
    var2 = 1
    print(var1, var2, end = ', ')

    for i in range(1, n):
        temp = var1
        var1 = var2
        var2 = var1 + temp
        print(var2, end = ', ')

Fibbo(5)
