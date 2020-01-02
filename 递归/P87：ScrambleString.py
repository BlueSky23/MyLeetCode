from collections import Counter

# 思路：搞清楚问题的本质，找一个分割点，前后部分对应转为字问题
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if len(s1) <= 2:
            return s1 == s2 or s1 == s2[::-1]
        # 找到分割点，有两种可能，s1的前、后部分分别与s2的前、后部分对应，
        # 或者s1的前、后部分分别与s2的后、前部分对应
        for i in range(1, len(s1)):
            pre1, post1 = s1[:i], s1[i:]
            pre2, post2 = s2[:i], s2[i:]
            # 只有对应部分的字母个数都相同时再去判断
            if Counter(pre1) == Counter(pre2) and Counter(post1) == Counter(post2):
                if self.isScramble(pre1, pre2) and self.isScramble(post1, post2):
                    return True
            pre2, post2 = s2[:len(s1) - i], s2[len(s1) - i:]
            if Counter(pre1) == Counter(post2) and Counter(post1) == Counter(pre2):
                if self.isScramble(pre1, post2) and self.isScramble(post1, pre2):
                    return True

        return False
