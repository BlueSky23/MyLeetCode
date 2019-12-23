class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return

        intervals = sorted(intervals, key=lambda x: x[0])

        ret = []
        cur_interval = intervals[0]
        for interval in intervals:
            begin, end = interval
            # 完全覆盖
            if end <= cur_interval[1]:
                continue
            # 交叉
            elif begin <= cur_interval[1] and end >= cur_interval[1]:
                tmp_min = min(begin, cur_interval[0])
                tmp_max = max(end, cur_interval[1])
                cur_interval = tmp_min, tmp_max
            # 没交叉
            else:
                ret.append(cur_interval)
                cur_interval = interval

        ret.append(cur_interval)

        return ret
