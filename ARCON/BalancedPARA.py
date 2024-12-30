def balanced(string: str) -> bool:
    stack = []
    dictionary = { '}':'{', ']': '[', ')': '('}
    for chr_ind in range(len(string)):
        char = string[chr_ind]
        if char in dictionary:
            if stack and stack[-1] == dictionary[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)

    if not stack:
        return True
    else:
        return False


print(balanced('[[]((([[]]))){[]}]'))
print(balanced('[[]((([[]]))){[{]}]'))
                