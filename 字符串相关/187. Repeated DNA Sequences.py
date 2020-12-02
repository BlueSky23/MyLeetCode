class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return None

        dictionary = {}
        for i in range(len(s) - 9):
            if s[i:i + 10] in dictionary:
                dictionary[s[i:i + 10]] += 1
            else:
                dictionary[s[i:i + 10]] = 1

        return [i for i in dictionary.keys() if dictionary[i] > 1]
