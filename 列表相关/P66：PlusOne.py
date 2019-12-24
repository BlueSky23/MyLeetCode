class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return
        # 先计算最后一位加1
        s, carry = (digits[-1] + 1) % 10, (digits[-1] + 1) // 10
        digits[-1] = s
        # 如果有进位，一次计算后续位与进位的和
        for i in range(len(digits) - 2, -1, -1):
            if carry:
                s, carry = (digits[i] + carry) % 10, (digits[i] + carry) // 10
                digits[i] = s
            else:
                break
        # 如果最后有进位，在首位置插入
        if carry:
            digits[0:0] = [carry]

        return digits