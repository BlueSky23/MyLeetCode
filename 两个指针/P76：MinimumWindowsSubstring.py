# 学习双指针－－》滑动窗口
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 检查已有的字母串是否已包含了所有目标字母
        def santisfy(having, target):
            if len(having) != len(target):
                return False
            for c in target:
                if target[c] > having[c]:
                    return False
            return True

        # 空串
        if not s or not t:
            return ''
        # 使用字典统计来判断是否包含了所有目标字母
        import collections
        target = collections.Counter(t)
        having = {}
        # 两组双指针，一组用来遍历，一组用来记录最短的满足要求的字符串
        left, right = 0, len(s) - 1
        i, j = 0, 0
        while j < len(s):
            # 每次碰到一个目标字母，通过右移i找到以j结尾的最短满足要求的字符串
            if s[j] in t:
                if s[j] in having:
                    having[s[j]] += 1
                else:
                    having[s[j]] = 1
                # 通过移动i检查以j结尾的最短字符串
                while i < j:
                    if s[i] in t:
                        having[s[i]] -= 1
                        if santisfy(having, target):
                            i += 1
                        else:
                            having[s[i]] += 1
                            break
                    else:
                        i += 1
                # 更新left和right
                if santisfy(having, target):
                    if j - i < right - left:
                        left, right = i, j
            # j右移
            j += 1

        if santisfy(having, target):
            return s[left:right + 1]
        else:
            return ''




