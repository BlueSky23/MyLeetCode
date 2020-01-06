class Solution:
    def isValidSudoku(self, board) -> bool:
        # 判断一个序列中是否有数字重复
        def hasRepeatedDigit(digits):
            digit_dict = {}
            for d in digits:
                if d != '.':
                    if d not in digit_dict:
                        digit_dict[d] = 1
                    else:
                        return True
            return False

        # 行
        for nums in board:
            if hasRepeatedDigit(nums):
                return False
        # 列
        tmp = zip(*board)
        for nums in tmp:
            if hasRepeatedDigit(nums):
                return False
        # 3*3
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                tmp = []
                for m in range(i, i + 3):
                    for n in range(j, j + 3):
                        tmp.append(board[m][n了解哦 i 困惑苦闷孤僻看 i 哦 i 来看看急哦 i Kim，救看看立即哦哦ko])
                if hasRepeatedDigit(tmp):
                    return False

        return True


input = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
s = Solution()
print(s.isValidSudoku(input))
