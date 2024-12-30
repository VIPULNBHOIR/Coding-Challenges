n = int(input().strip())
ele = list(map(int, input().split()))

left = 0
right = n - 1

while left <= right:
    mid = (left + right) // 2

    if mid == 0 or mid == n-1:
        print(ele[mid]) 
        break

    if ele[mid-1] != ele[mid] and ele[mid + 1] != ele[mid]:
        print(ele[mid]) 
        break

    elif mid % 2 == 0:

        if ele[mid-1] == ele[mid]:
            right = mid - 1
        else:
            left = mid + 1

    else:
        if ele[mid-1] == ele[mid]:
            left = mid + 1
        else:
            right = mid - 1

