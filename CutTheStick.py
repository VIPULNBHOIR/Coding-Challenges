total = 0
cuts = [1,5,3,8]
cuts = set(cuts)
n = 9

def f(start, end):
    global total
    if end - start <= 1: 
        return 

    m = (start +  end) // 2

    if m in cuts:
        total += (end - start)
        f(start, m)
        f(m, end)
        

    else:
        left = m - 1
        right = m + 1
        while cuts and left > start and right < end:
            if right in cuts:
                total += (end - start)
                f(start, right)
                f(right, end)
                return

            elif left in cuts:
                total += (end - start)
                f(start, left)
                f(left, end)
                return

            left -= 1
            right += 1

    return

f(0, n)
print(total)