from typing import List

class LargestNumber:
    
    def largest_number(arr: List[str]) -> str:
        # Custom comparison key function
        def custom_key(num: str) -> str:
            print(num + num[::-1])
            return num + num[::-1]  # Reversing ensures correct string comparison for numbers like "30" and "3"

        # Sort the array of strings using the custom key function
        arr.sort(key=custom_key, reverse=True)
        print(arr)

        # If the largest number is 0, return "0"
        if arr[0] == "0":
            return "0"

        # Concatenate the sorted strings to form the largest possible number
        result = ''.join(arr)

        return result

# Test cases
arr1 = ["35", "30", "34", "5", "9"]
print("Output for arr1:", LargestNumber.largest_number(arr1)) # Output: "9534330"

arr2 = ["8","9","55","550"]
print("Output for arr2:", LargestNumber.largest_number(arr2)) # Output: "6054854654"
