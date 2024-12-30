class Solution:
	def Uniquemaxsubstring(self, string: str)-> int:
		map = {}
		maxi = float('-inf')
		i=j = 0
		for pos, char in enumerate(string):
			if char in map and map[char] >= i:

				maxi = max(maxi, pos-i )
				i = map[char] + 1

			map[char] = pos
			

		print(i, pos+1)
		return max(maxi, pos+1 - i)

string = str(input())
print(Solution().Uniquemaxsubstring(string))

				

			

