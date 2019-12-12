# 主要理解：只要串中满足到任意位置都有左括号数量大于等于右括号数量，则串为合法。
#  所以对n-1情况中的有效串，我们可以在任意位置插入'('，再在最后补上')'，仍可以构成有效串
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ['()']
        result = set()
        # 递归解决n-1的情况
        tmp = self.generateParenthesis(n - 1)
        # 对n-1的每一个合法的串，从左到右逐次插入'('并把')'放到最后，保证对每一个子串都有左括号的数量大于右括号的数量
        for valid_p in tmp:
            for i in range(len(valid_p) + 1):
                result.add(valid_p[:i] + '(' + valid_p[i:] + ')')

        return list(result)