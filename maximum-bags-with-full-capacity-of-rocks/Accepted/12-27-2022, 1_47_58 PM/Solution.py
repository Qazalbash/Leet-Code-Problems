// https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        towers = sorted([(capacity[i] - rocks[i], capacity[i], rocks[i])
                for i in range(len(capacity))],
                key=lambda x: x[0])

        count = 0
        for i in range(len(towers)):
            if towers[i][0] == 0:
                count += 1
            elif towers[i][0] <= additionalRocks:
                count += 1
                additionalRocks -= towers[i][0]
            else:
                break

        return count