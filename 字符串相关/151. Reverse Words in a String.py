class Solution:
    def reverseWords(self, s: str) -> str:
        tmp=[word for word in s.split(' ') if word]
        tmp=tmp[::-1]
        return ' '.join(tmp)