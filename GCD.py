num1, num2 = map(int, input().split())

mini = min(num1, num2)
maxi = max(num1, num2)
flag = 0

if maxi % mini == 0:
    print(mini)
    flag = 1
    
else:    
    for i in range(2, int(mini ** 0.5) + 1):
        if num1 % i == 0:
            cotient = num1 // i

            if num1 % cotient == 0 and num2 % cotient == 0:
                print(cotient)
                flag = 1
                break

            elif num1 % i == 0 and num2 % i == 0:
                print(i)
                flag = 1
                break

if not flag:
    print(1)




