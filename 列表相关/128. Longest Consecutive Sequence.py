# 充分利用字典、集合等hash数据结构
# 思路：给定一个数，向上、向下找到所有连续的序列，并对找到的数标记，不再处理

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # 记录连续数字序列
        dictionary = {}
        # 用于检索是否存在
        dict_nums = set(nums)

        for n in nums:
            # 对未处理的数字
            if n in dict_nums:
                dictionary[n] = [n]
                dict_nums.remove(n)
                # 向下
                tmp = n - 1
                while True:
                    if tmp in dict_nums:
                        dictionary[n].append(tmp)
                        dict_nums.remove(tmp)
                        tmp -= 1
                    else:
                        break
                # 向上
                tmp = n + 1
                while tmp in dict_nums:
                    if tmp in dict_nums:
                        dictionary[n].append(tmp)
                        dict_nums.remove(tmp)
                        tmp += 1
                    else:
                        break

            else:
                pass

        # 取最长的序列
        maxLen = 0
        for key in dictionary:
            maxLen = max(maxLen, len(dictionary[key]))

        return maxLen
