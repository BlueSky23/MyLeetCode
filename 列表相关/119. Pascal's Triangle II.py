class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 0:
            return []
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]

        pre = [1, 1]
        for i in range(2, rowIndex + 1):
            tmp = [1]
            for i in range(len(pre) - 1):
                tmp.append(pre[i] + pre[i + 1])
            tmp.append(1)
            pre = tmp

        return pre
