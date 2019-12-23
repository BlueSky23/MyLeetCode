# 思路，两个区间的覆盖分为三种情况：
# 1、在前
# 2、中间交叉，结果未min_x,max_y
# 3、在后
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        if not newInterval:
            return intervals

        i = 0
        while i < len(intervals):
            new_min, new_max = newInterval
            interval = intervals[i]
            # 在当前区间之前，直接插入返回
            if new_max < interval[0]:
                flag = True
                intervals[i:i] = [newInterval]
                return intervals
            # 没重合，检查下一个区间
            elif new_min > interval[1]:
                i += 1
                continue
            else:
                tmp_min = min(new_min, interval[0])
                tmp_max = max(new_max, interval[1])
                newInterval = [tmp_min, tmp_max]
                intervals.remove(interval)

        intervals.append(newInterval)

        return intervals
