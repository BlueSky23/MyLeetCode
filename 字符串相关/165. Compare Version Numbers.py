class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # 归一化到整数列表
        ver1 = [int(i) for i in version1.split('.')]
        ver2 = [int(i) for i in version2.split('.')]
        # 长度相同
        if len(ver1) < len(ver2):
            for i in range(len(ver2) - len(ver1)):
                ver1.append(0)
        else:
            for i in range(len(ver1) - len(ver2)):
                ver2.append(0)

        # 逐项比较
        for i in range(len(ver1)):
            if ver1[i] == ver2[i]:
                continue
            elif ver1[i] < ver2[i]:
                return -1
            else:
                return 1

        return 0
