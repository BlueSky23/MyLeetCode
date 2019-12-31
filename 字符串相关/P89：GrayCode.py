# 思路：确定总数后，一个一个找
class Solution:
    def grayCode(self, n: int) -> List[int]:

        if n == 0:
            return [0]
        # 字典用于查重
        ret = {'0' * n: 0}
        cnt = 1
        tmp = list('0' * n)
        # 总个数确定为2的n次方
        while (cnt < 2 ** n):
            # 逐个变化一位，检查是否已在结果集合中
            for i in range(n - 1, -1, -1):
                tmp[i] = '1' if tmp[i] == '0' else '0'
                if ''.join(tmp) not in ret:
                    ret[''.join(tmp)] = cnt
                    cnt += 1
                    break
                # 如果已在，则恢复tmp
                tmp[i] = '1' if tmp[i] == '0' else '0'
        # 按添加顺序排序
        ret = sorted(ret, key=lambda x: ret[x])
        # 二进制转化为整型
        ret = [int(i, 2) for i in ret]

        return ret
