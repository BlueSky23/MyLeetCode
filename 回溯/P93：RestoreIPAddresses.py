class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # dfs 遍历
        def dfs(s, path, ret):
            # ip长度不够或超长了
            if not s:
                return
            # 找到合适的IP，添加到结果集
            elif path.count('.') == 3 and int(s) < 256:
                if (len(s) == 1) or (len(s) == 2 and s[0] != '0') or (len(s) == 3 and s[0] != '0' and s[:2] != '00'):
                    path += '.' + s
                    ret.append(path[1:])
                    return
            # 逐步遍历
            elif path.count('.') < 3:
                tmp = path
                tmp += '.' + s[0]
                dfs(s[1:], tmp, ret)

                if len(s) >= 2 and s[0] != '0':
                    tmp = path
                    tmp += '.' + s[:2]
                    dfs(s[2:], tmp, ret)

                if len(s) >= 3 and int(s[:3]) < 256 and s[0] != '0' and s[:2] != '00':
                    tmp = path
                    tmp += '.' + s[:3]
                    dfs(s[3:], tmp, ret)
            # 不符合IP格式
            else:
                return

        # 特殊情况
        if not s or len(s) < 4:
            return []

        ret = []
        # dfs遍历
        dfs(s, "", ret)
        return ret