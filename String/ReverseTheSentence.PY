class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the input string by whitespace and remove leading/trailing spaces
        words = s.strip().split()

        # Reverse the list of words and join them with a single space
        return ' '.join(words[::-1])

