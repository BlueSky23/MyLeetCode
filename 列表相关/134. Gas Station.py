# 关键一个思路：如果idx1是满足gas>=cost的，后面在idx2处不满足sum_gas>=sum_cost,
# 则idx1和idx2之间的位置一定都不满足

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 如果需求总量大于gas总量，无解
        if sum(cost) > sum(gas):
            return -1
        # 循环遍历起点
        idx = 0
        while idx < len(gas):
            if gas[idx] >= cost[idx]:
                sum_gas, sum_cost = 0, 0
                # 遍历数列后半部分
                i = idx
                while i < len(gas) and sum_gas >= sum_cost:
                    sum_gas += gas[i]
                    sum_cost += cost[i]
                    i += 1
                # 不满足，直接跳到i索引处
                if sum_gas < sum_cost:
                    idx = i
                    continue

                # 遍历数列前半部分
                i = 0
                while i < idx and sum_gas >= sum_cost:
                    sum_gas += gas[i]
                    sum_cost += cost[i]
                    i += 1
                # 不满足，则后续的索引一定都不满足
                if sum_gas < sum_cost:
                    return -1

                return idx

            idx += 1

        return -1
