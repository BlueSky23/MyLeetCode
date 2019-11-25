class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_str = s[0]
        temp_str = s[0]
        for character in s:
            if character not in temp_str:
                temp_str += character
            else:
                # 更新最大子串
                if len(temp_str) > len(max_str):
                    max_str = temp_str
                # 更新临时串
                temp_idx = temp_str.index(character)
                temp_str = temp_str[temp_idx + 1:] + character

        if len(temp_str) > len(max_str):
            max_str = temp_str

        return len(max_str)
