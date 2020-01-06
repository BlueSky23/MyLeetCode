class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []
        # 特殊情况
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        ret = [[1], [1, 1]]
        for i in range(3, numRows + 1):
            # 第一个元素
            tmp = [1]
            # 中间元素由上一个列表的元素和得到
            for i in range(len(ret[-1]) - 1):
                tmp.append(ret[-1][i] + ret[-1][i + 1])
            # 最后一个元素
            tmp.append(1)
            ret.append(tmp)

        return ret
