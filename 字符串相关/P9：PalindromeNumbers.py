# Follow up: without converting the integer to a string

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        # 逐个保存数字
        nums = []
        y = x
        while y != 0:
            digit = y % 10
            nums.append(digit)
            y = y // 10
        # 由单个数字复原整数
        num = 0
        for digit in nums:
            num = num * 10 + digit
        # 判断，输出
        if num == x:
            return True
        else:
            return False
