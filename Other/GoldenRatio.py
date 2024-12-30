ratio=[1,]
i=1

def fibbo(a,b):
    global i
    if len(ratio)==29:
        return
    else:
        ratio.append((a+b)/a)
        i+=1
        print(a+b, end=" ")
        fibbo(b,a+b)

    return ratio

print("fibbo series: 1 1",end=" ")
list1=fibbo(1,1)

print()
print("\nratios: ", list1)