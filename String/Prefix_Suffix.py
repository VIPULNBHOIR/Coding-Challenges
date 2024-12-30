class Solution:
    def minimumLength(self, s: str) -> int:

        left, right = 0, len(s) - 1
        result = len(s)

        while left < right:
            while left < right and s[left] == s[left + 1]:
                left += 1

            while right > left and s[right] == s[right - 1]:
                right -= 1

            if s[left] == s[right]:
                result = right - left - 1
            else:
                break

            left += 1
            right -= 1

        return 0 if result < 0 else result


        