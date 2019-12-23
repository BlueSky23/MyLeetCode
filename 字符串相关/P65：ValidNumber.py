class Solution:
    def isNumber(self, s: str) -> bool:
        def onlyDigits(s):
            if not s:
                return False
            digits = [str(i) for i in range(10)]
            for d in s:
                if d not in digits:
                    return False
            return True

        s = s.strip()
        if not s:
            return

        if s[0] == '+' or s[0] == '-':
            if 1 in range(len(s)) and (onlyDigits(s[1]) or s[1] == '.'):
                return self.isNumber(s[1:])
            else:
                return False
        elif 'e' in s:
            idx = s.index('e')
            if idx == len(s) - 1:
                return False
            if '.' in s[:idx]:
                tmp_idx = s[:idx].index('.')
                return (not s[:tmp_idx] or onlyDigits(s[:tmp_idx])) and (
                        not s[tmp_idx + 1:idx] or onlyDigits(s[tmp_idx + 1:idx])) and (
                               s[:tmp_idx] or s[tmp_idx + 1:idx]) and (
                               onlyDigits(s[idx + 1:]) or (s[idx + 1] in ['+', '-'] and onlyDigits(s[idx + 2:])))
            else:
                return onlyDigits(s[:idx]) and (
                        onlyDigits(s[idx + 1:]) or (s[idx + 1] in ['+', '-'] and onlyDigits(s[idx + 2:])))
        elif '.' in s:
            idx = s.index('.')
            return (not s[:idx] or onlyDigits(s[:idx])) and (not s[idx + 1:] or onlyDigits(s[idx + 1:])) and (
                    s[:idx] or s[idx + 1:])
        else:
            return onlyDigits(s)
