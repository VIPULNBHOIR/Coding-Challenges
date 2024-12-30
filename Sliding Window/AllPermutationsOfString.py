from collections import Counter, deque

class Solution:
	def findSubstring(self, s: str, words: list[str]) -> list[int]:
		k = len(words[0])
		dictionary = Counter(words)
		map = {}
		window=deque() 
		visisted = set() 
		res = []
		i = 0
		while i < len(s):
			word = s[i: i+k]

			if word in dictionary:

				if word not in map:
					map[word] = 1
					window.append((word, i))

				elif map[word] < dictionary[word]:
					map[word] += 1
					window.append((word, i))
					
				elif map[word] >= dictionary[word]:
					while window and window[0][0] != word:
						prev_word, pos = window.popleft()
						map[prev_word] -= 1

					if window:
						prev_word, pos = window.popleft()
						map[prev_word] -= 1

						window.append((word, i))
						map[word] += 1


				if len(window) == len(words):
					phrase = s[window[0][1] : window[len(words)-1][1]]	
					if phrase not in visisted:
						res.append(window[0][1])
						visisted.add(phrase)

					prev_word, pos = window.popleft()
					map[prev_word] -= 1	

				i += k

			else:
				i += 1
				while window:
					prev_word, pos = window.popleft()
					map[prev_word] -= 1

		return res

			
print(Solution().findSubstring("wordgoodgoodgoodbestword",  ["word","good","best","word"]))

print(Solution().findSubstring("barfoofoobarthefoobarman",["bar","foo","the"]))

print(Solution().findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake",words =["fooo","barr","wing","ding","wing"]))
