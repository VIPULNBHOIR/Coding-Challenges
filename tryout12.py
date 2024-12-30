# Python 3 implementation

def findFlowerIndexes(n, t, arr):
    mini = 0
    maxi = n-1

    while mini < maxi:
        req = arr[mini] + arr[maxi]
        if req == t:
            while maxi != mini + 1 and arr[maxi] == arr[maxi-1]:
                maxi -= 1

            return mini, maxi
    

        elif req > t:
            maxi -= 1
        
        else:
            mini += 1

    # User will write the logic here
    return -1, -1  # Placeholder return, user will modify this

if __name__ == "__main__":
    n, t = map(int, input().split())
    arr = list(map(int, input().split()))
    result = findFlowerIndexes(n, t, arr)
    print(result[0], result[1])
