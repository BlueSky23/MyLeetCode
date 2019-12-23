class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return
        if len(nums) == 1:
            return True
        queue = [0]
        # 标志该位置是否处理过
        flag = [False] * len(nums)
        flag[0] = True
        while queue:
            idx = queue.pop(0)
            for i in range(nums[idx], 0, -1):
                if idx + i >= len(nums) - 1:
                    return True
                # 如果未处理，则入队列等待处理
                if not flag[idx + i]:
                    queue.append(idx + i)
                    flag[idx + i] = True
                # 如果当前节点已经处理，则比它小的节点也一定处理过，不再处理
                else:
                    break

        return False

