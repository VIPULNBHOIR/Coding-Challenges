from collections import deque

class Solution:
	def Subarray(self, target, nums):
		least = float('inf')
		count = sum = 0

		window = deque()
		for num in nums:
			if num == target:
				return 1
			else:
				window.append(num)
				print(window)
				sum += num
				count += 1
				
				while sum >= target:
					least = min(least, count)
					sum -= window.popleft()
					print(window)
					count -= 1
					
		if least == float('inf'):
			return 0

		return least

print(Solution().Subarray(11,[1,1,1,1,1,1,1,1]))

