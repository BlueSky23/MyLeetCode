class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path:
            return
        # 方便后面统一处理
        path += '/'
        ret = path[0]
        begin, end = 1, 1
        while end < len(path):
            if path[end] != '/':
                end += 1
            else:
                # 当前目录，忽略
                if path[begin:end] == '.':
                    pass
                # 父目录
                elif path[begin:end] == '..':
                    if ret == '/':
                        pass
                    else:
                        tmp = len(ret) - 2
                        while tmp > 0:
                            if ret[tmp] != '/':
                                tmp -= 1
                            else:
                                break
                        ret = ret[:tmp + 1]

                # 具体目录
                else:
                    if begin == end:  # //
                        pass
                    else:
                        ret += path[begin:end + 1]

                begin = end + 1
                end = end + 1

        # 删除最后的/
        if len(ret) > 1 and ret[-1] == '/':
            ret = ret[:-1]
        return ret


s = Solution()
path = "/a//b////c/d//././/.."
print(s.simplifyPath(path))
