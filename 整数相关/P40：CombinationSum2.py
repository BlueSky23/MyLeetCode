class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 目标值不大于0
        if target <= 0:
            return
        # 数组为空
        if not candidates:
            return

        rs = []
        # 每一个元素都只有两种可能，出现（1）或不出现（0）
        for i in range(2):
            # 当前元素为target值
            if target - i * candidates[0] == 0:
                rs.append([candidates[0]])
                continue
            tmp = self.combinationSum2(candidates[1:], target - i * candidates[0])
            if tmp:
                # 对子问题的每一个解判断是否加入当前元素
                for comb in tmp:
                    # 加入或不加入当前元素candidates[0]
                    for j in range(i):
                        comb.append(candidates[0])
                    rs.append(comb)
        # 去重
        if rs:
            rs = [tuple(sorted(item)) for item in rs]
            rs = list(set(rs))
            rs = [list(item) for item in rs]
        return rs