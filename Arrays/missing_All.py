def findDisappearedNumbers(nums):

    for num in nums:
        index = abs(num) - 1
        nums[index] = -abs(nums[index])

    print(nums)

    missing_numbers = [i + 1 for i, num in enumerate(nums) if num > 0]

    return missing_numbers

# Test cases
nums1 = [1,4, 3, 2, 7, 8, 2, 3, 5]
print(findDisappearedNumbers(nums1))  # Output: [5, 6]

nums2 = [1, 1]
print(findDisappearedNumbers(nums2))  # Output: [2]


# O(n)