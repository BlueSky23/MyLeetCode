class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def helper(start, prerequisites, finishedcourses, dp):
            b = True
            for item in prerequisites:
                if item[0] == start:
                    if item[1] not in finishedcourses:
                        if dp[item[1]] == 1:
                            continue
                        else:
                            b = b and helper(item[1], prerequisites, finishedcourses + [item[1]], dp)
                    else:
                        return False
            return b

        dp = [-1] * numCourses
        for i in range(numCourses):
            if not helper(i, prerequisites, [i], dp):
                dp[i] = False
                return False
            else:
                dp[i] = 1

        return True

