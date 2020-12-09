'''
思路：1、helper方法判断从某一个指定的course开始是否有环；
    2、判断每一个course开始是否有环
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # # from a specified course
        # def helper(start, prerequisites, finishedcourses, dp):
        #     b = True
        #     for item in prerequisites:
        #         if item[0] == start:
        #             if item[1] not in finishedcourses:
        #                 if dp[item[1]] == 1:
        #                     continue
        #                 else:
        #                     b = b and helper(item[1], prerequisites, finishedcourses + [item[1]], dp)
        #             else:
        #                 return False
        #     return b
        # # all courses
        # dp = [-1] * numCourses
        # for i in range(numCourses):
        #     if not helper(i, prerequisites, [i], dp):
        #         dp[i] = False
        #         return False
        #     else:
        #         dp[i] = 1
        #
        # return True

        # topological sort
        class Solution:
            def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
                degree = [0] * numCourses
                adjacent = [set() for i in range(numCourses)]
                q = [i for i in range(numCourses)]
                for item in prerequisites:
                    degree[item[1]] += 1
                    adjacent[item[0]].add(item[1])
                    if item[1] in q:
                        q.remove(item[1])

                cnt = 0
                while len(q) > 0:
                    hasZero = False
                    course = q.pop(0)
                    cnt += 1
                    for item in adjacent[course]:
                        degree[item] -= 1
                        if degree[item] == 0:
                            q.append(item)
                            hasZero = True

                if cnt == numCourses:
                    return True
                else:
                    return False



