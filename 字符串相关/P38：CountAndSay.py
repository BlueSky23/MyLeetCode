class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 0:
            return
        if n == 1:
            return '1'
        rs = ''
        # 获取前一个串
        tmp = self.countAndSay(n - 1)
        # 基于前一个串，统计得到当前串
        cnt = 1
        for i in range(1, len(tmp)):
            if tmp[i] == tmp[i - 1]:
                cnt += 1
            else:
                rs += str(cnt) + tmp[i - 1]
                cnt = 1
        # for循环没有处理最后一个字符，补充
        rs += str(cnt) + tmp[-1]

        return rs
