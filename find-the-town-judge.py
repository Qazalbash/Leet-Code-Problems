// https://leetcode.com/problems/find-the-town-judge

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        count = dict()
        max_trust = 0
        judge = -1
        for villager, trustworthy in trust:
            count[trustworthy] = count.get(trustworthy, []) + [villager]
        print(count)
        for villager, trustworthy in count.items():
            if len(count[villager]) + 1 == n:
                for i in count[villager]:
                    if villager in count.get(i, []):
                        return -1
                return villager
        return -1