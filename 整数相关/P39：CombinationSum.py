class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 数组为空
        if not candidates:
            return
        if target == 0:
            return
        # 数组只有一个元素，target需为该元素的整数倍
        if len(candidates) == 1:
            if target < candidates[0]:
                return
            rs = []
            if target % candidates[0] == 0:
                while target - candidates[0] >= 0:
                    rs.append(candidates[0])
                    target -= candidates[0]
                return [rs]
            return

        rs = []
        # 递归求解，用整除计算第一个元素最多取多少次
        tmp = target // candidates[0]
        for i in range(tmp + 1):
            if target - i * candidates[0] < 0:
                return
            # 找到答案
            if target - i * candidates[0] == 0:
                tt = []
                for j in range(i):
                    tt.append(candidates[0])
                rs.append(tt)
            # 第1个元素取i次，递归求解后续
            tmp_recur = self.combinationSum(candidates[1:], target - i * candidates[0])
            if tmp_recur:
                # 将当前元素附加到子问题的解中
                for tt in tmp_recur:
                    for j in range(i):
                        tt.append(candidates[0])
                    rs.append(tt)

        return rs