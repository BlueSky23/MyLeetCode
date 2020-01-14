# 思路，基于BFS，记录每一个节点的前序节点，最后再构造路径
# 由于只求最短的可能路径，因此每个节点的前序节点只能来自前一层

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        if endWord not in wordList:
            return []

        wordList = set(wordList)
        # 保存已遍历过的节点
        visited = {beginWord}
        # 保留访问顺序对，为后面构造路径做准备
        path = {}
        path[beginWord] = [None]

        q = [beginWord]
        while q:
            level = []
            # 前序节点只从上一层中的节点中添加
            for tmp in q:
                # 找出可能的后继单词
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    for i in range(len(beginWord)):
                        word = tmp[:i] + c + tmp[i + 1:]
                        # 在wordlist中
                        if word in wordList and word not in visited:
                            if word in path and tmp not in path[word]:
                                path[word].append(tmp)
                            elif word not in path:
                                path[word] = [tmp]
                            level.append(word)
            for word in level:
                visited.add(word)

            q = level

        print(path)

        # 结果列表
        ret = [[endWord]]
        # 没有找到
        if endWord not in path:
            return []
        # 从path构造结果路径
        while True:
            tmp1 = []
            for p in ret:
                if path[p[0]] == [None]:
                    return ret
                # 对每一个前边的节点，扩充路径
                for word in path[p[0]]:
                    if word and word not in p:
                        tmp2 = list(p)
                        tmp2 = [word] + tmp2
                        tmp1.append(tmp2)
            ret = tmp1
