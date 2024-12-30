def GCD(num1, num2):
    if not num2 % num1:
        return num1
    
    for num in range(2, int(num1 ** 0.5) + 1):
        if not num1 % num:
            cotient = num1 // num 
            if not num1 % cotient and not num2 % cotient:
                return cotient

            if not num1 % i and not num2 % i:
                return i

    return 1

num1, num2 = map(int, input().split())

mini = min(num1, num2)
maxi = max(num1, num2)

lcm = int(mini * maxi / GCD(mini, maxi))

print(lcm)

