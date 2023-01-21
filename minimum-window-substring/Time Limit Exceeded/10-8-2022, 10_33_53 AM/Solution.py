// https://leetcode.com/problems/minimum-window-substring

from collections import Counter


class Solution:

    def minWindow(self, s: str, t: str) -> str:
        max_size = len(s) + 1
        real_ele_counter = Counter(t)
        for win_size in range(len(t), max_size):
            win_list = [s[i:i + win_size] for i in range(max_size - win_size)]
            for win_ele in win_list:
                win_ele_counter = Counter(win_ele)
                if all(real_ele_counter[k] <= win_ele_counter[k] for k in t):
                    return win_ele
        return ""