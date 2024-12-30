from collections import Counter

class Solution:
	def numberofpermutationexists(string, words):
		words = set(words)
		map = {} #count and index of the word
		req_index = 0
		dictionary = Counter(words)
		for i in range (0,len(string),len(words[0])):
			curr_word = string[i:len(words[0])]

			if curr_word in words and map[curr_word][0] <= dictionary[curr_word] :
				last_index = map[curr_word]
				if last_index < req_index:
					map[curr_word][1] = i
					map[curr_word][0] = 1
				else:
					map[curr_word][0] += 1

			elif curr_word in words:
				map[curr_word][1] = i
				map[curr_word][0] = 1


			else:
				req_index = 0
							
		