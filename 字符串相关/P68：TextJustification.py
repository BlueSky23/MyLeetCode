# 没有技巧，就是一行行判断输出
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        ret = []
        begin, idx = 0, 0
        # 循环整个单词列表
        while idx < len(words):
            # 找到放入一行的单词组
            lineNo = 0
            # 单词数+空格数小于maxWidth
            while idx < len(words) and lineNo + (idx - 1 - begin) < maxWidth:
                lineNo += len(words[idx])
                idx += 1

            if lineNo + (idx - begin - 1) >= maxWidth:
                # 每个单词加一个空格，正好凑够maxwidth
                if lineNo + (idx - begin - 1) == maxWidth:
                    ret.append(' '.join(words[begin:idx]))
                    idx -= 1
                else:
                    # idx指向写入本行的最后一个单词的下一个单词
                    idx -= 1
                    words_length = lineNo - len(words[idx])
                    # idx 指向写入本行的最后一个单词
                    idx -= 1
                    # 计算空格数
                    if idx == begin:
                        tmp = words[idx] + ' ' * (maxWidth - len(words[idx]))
                    else:
                        base = (maxWidth - words_length) // (idx - begin)
                        remainer = (maxWidth - words_length) % (idx - begin)
                        tmp = ''
                        # 按空格数和单词数布局
                        for i in range(begin, idx):
                            tmp += words[i] + ' ' * base
                            if remainer:
                                tmp += ' '
                                remainer -= 1
                        tmp += words[idx]

                    ret.append(tmp)
            # idx到头，最后一行单词数不够
            else:
                idx -= 1
                # 计算空格数
                if idx == begin:
                    tmp = words[idx] + ' ' * (maxWidth - len(words[idx]))
                else:
                    tmp = ''
                    # 按空格数和单词数布局
                    for i in range(begin, idx):
                        tmp += words[i] + ' '

                    tmp += words[idx]
                    tmp += ' ' * (maxWidth - len(tmp))

                ret.append(tmp)

            idx += 1
            begin = idx

        return ret
