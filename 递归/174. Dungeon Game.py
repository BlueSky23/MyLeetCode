class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        if len(dungeon) == 0 or len(dungeon[0]) == 0:
            return
        m, n = len(dungeon), len(dungeon[0])
        if n == 1:
            s = 0
            for l in dungeon:
                s += l[0]
            return s
        elif m == 1:
            return sum(dungeon[0])

        dungeon_right = []
        for i in range(0, len(dungeon)):
            dungeon_right.append(list(dungeon[i][1:]))
        dungeon_down = []
        for i in range(1, len(dungeon)):
            dungeon_down.append(list(dungeon[i]))

        print(dungeon_right, dungeon_down)

        m = min(self.calculateMinimumHP(dungeon_right), self.calculateMinimumHP(dungeon_down))

        return m + dungeon[0][0]


s=Solution()
# metrics=[[-2,-3,3],[-5,-10,1],[10,30,-5]]
metrics=[[-10,1],[30,-5]]
minhealth=s.calculateMinimumHP(metrics)
print(minhealth)