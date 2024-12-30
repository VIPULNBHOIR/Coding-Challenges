def Rotate_left(nums: list[list[int]]) -> list[list[int]]:      #ONLY APPLICABLE FOR QUBE
    n=len(nums)
    newArray=[[0]*n for _ in range(n)]

    for col in range(n-1,-1,-1):
        for row in range(0,n):
            newArray[n-1-col][row]=nums[row][col]

    return newArray

def Print(arr):
    for i in range(len(arr)):
        print(arr[i])

    print()


rotation1=Rotate_left([[1,2,3],[4,5,6],[7,8,9]])
Print(rotation1)

rotation2=Rotate_left(rotation1)
Print(rotation2)

rotation3=Rotate_left(rotation2)
Print(rotation3)

rotation4=Rotate_left(rotation3)
Print(rotation4)