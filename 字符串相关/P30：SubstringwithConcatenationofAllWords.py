# 由于输入的words长度都相同，因此在将s划分为word时，起始位置只有size种可能
# 当起始位置选size＋1时与选1时，划分结果一样
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return

        words.sort()
        length, size = len(words), len(words[0])
        rs = []
        # 要把字符串划分成长度为size的words，起点位置只有size种可能
        for j in range(size):
            tmp_list = []
            idx = j
            # 针对每一种可能，持续获取len(words)个长度为size的words，并与输入的words比对

            for i in range(j, len(s), size):
                if len(tmp_list) < length:
                    tmp_list.append(s[i:i + size])
                if len(tmp_list) == length:
                    tmp = sorted(tmp_list)
                    # 比对成功，记录起始的idx
                    if tmp == words:
                        rs.append(idx)
                    # 移向下一个word
                    idx += size
                    tmp_list.pop(0)

        return rs
