class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 数字和字母的对应关系
        dict = {'2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']
                }
        result = []

        if not digits:
            return
        # 递归终止条件
        if len(digits) == 1:
            return dict[digits[0]]

        for d in dict[digits[0]]:
            for s in self.letterCombinations(digits[1:]):
                result.append(d + s)

        return result
