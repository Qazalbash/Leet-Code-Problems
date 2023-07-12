// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

class Solution {
public:
    int strStr(string haystack, string needle) {
        const int index = haystack.find(needle);
        if (index == string::npos) {
            return -1;
        }
        return index;
    }
};