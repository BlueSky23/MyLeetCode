class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left, right = ['(', '[', '{'], [')', ']', '}']
        for c in s:
            # 左边符号，进栈
            if c in left:
                stack.append(c)
            # 右边符号，出栈
            if c in right:
                # 先进来的右边符号
                if not stack:
                    return False
                tmp = stack.pop()
                # 如果不匹配，返回False
                if left.index(tmp) != right.index(c):
                    return False
        # 栈不为空，False
        if stack:
            return False

        return True


s = Solution()
print(s.isValid("()[]{}"))
